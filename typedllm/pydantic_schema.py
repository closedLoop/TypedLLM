import json
import re
from collections.abc import Iterable

from langchain.llms import OpenAI
from pydantic import BaseModel

from typedllm.prompt import FORMATTING_INSTRUCTIONS


def typedllm_call(task, callable_llm, pydantic_model: BaseModel):
    formatting_instructions = FORMATTING_INSTRUCTIONS.format(
        language="json", schema=generate_json_schema(pydantic_model)
    )
    prompt = f"{task}\n{formatting_instructions}\n# Markdown code snippet:\n"
    result = callable_llm(prompt)

    # TODO use markdown parser to extract code snippet blocks
    result = extract_code_from_response(result)

    stripped_lines = [
        re.sub(r'(?<![\'"])#.*$', "", line) for line in result.splitlines()
    ]
    result = "\n".join(stripped_lines)
    result_obj = json.loads(result.strip())

    # TODO try to dynamically set
    if isinstance(result_obj, dict):
        return pydantic_model(**result_obj)

    if isinstance(result_obj, (list, set, tuple)):
        return [pydantic_model(**o) for o in result_obj]

    return result_obj


def extract_code_from_response(code) -> str:
    code = re.sub(r"```[a-zA-Z]+[a-zA-Z0-9\-]*", "", code)
    if code.startswith("```"):
        code = code[3:]
    if code.endswith("```"):
        code = code[:-3]
    return code.strip()


def flatten_format_basemodel(pydantic_model, depth=1) -> Iterable[str]:
    if pydantic_model.get("type", None) == "object":
        properties = pydantic_model.get("properties", {})
        new_props = []
        for property_name, property_schema in properties.items():
            if property_schema.get("type", None) == "object":
                yield flatten_format_basemodel(property_schema, depth=depth + 1)

            # get properties
            is_required = property_name in pydantic_model.get("required", [])
            description = f"{property_schema.get('title','')} - {property_schema.get('description', '')}".strip().strip(
                " - "
            )
            datatype = f"{property_schema.get('type', '')}"
            if is_required:
                datatype += " (required)"
            row = property_name
            if datatype:
                row += f": {datatype}"
            if description:
                row += f" // {description}"
            new_props.append(row.strip())

    yield "# Type: " + pydantic_model.get("title", "Entity") + "\n{\n" + "\n".join(
        [" " * (depth * 4) + p for p in new_props]
    ) + "\n}\n"


def generate_json_schema(pydantic_model: BaseModel) -> str:
    schema = pydantic_model.schema()
    return "\n".join(list(flatten_format_basemodel(schema)))


def transform_schema(json_schema):
    return json_schema.replace('"', '\\"')


# Example usage
if __name__ == "__main__":
    from pydantic import BaseModel, Field

    task = "What is the personal information of Barack Obama?"
    llm = OpenAI(temperature=0)

    class ExampleModel(BaseModel):
        name: str = Field(..., description="Name of the user")
        age: int = Field(..., description="Age of the user")

    data = typedllm_call(task, llm, ExampleModel)
    print(data)
