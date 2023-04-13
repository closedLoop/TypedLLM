from langchain.chat_models import ChatOpenAI
from langchain.llms import OpenAI
from langchain.output_parsers import ResponseSchema, StructuredOutputParser
from langchain.prompts import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    PromptTemplate,
)


def main():
    response_schemas = [
        ResponseSchema(name="answer", description="answer to the user's question"),
        ResponseSchema(
            name="source",
            description="source used to answer the user's question, should be a website.",
        ),
    ]
    output_parser = StructuredOutputParser.from_response_schemas(response_schemas)

    format_instructions = output_parser.get_format_instructions()
    print(format_instructions)

    prompt = PromptTemplate(
        template="answer the users question as best as possible.\n{format_instructions}\n{question}",
        input_variables=["question"],
        partial_variables={"format_instructions": format_instructions},
    )

    model = OpenAI(temperature=0)

    _input = prompt.format_prompt(question="what's the capital of france")
    output = model(_input.to_string())

    output_parser.parse(output)

    chat_model = ChatOpenAI(temperature=0)

    prompt = ChatPromptTemplate(
        messages=[
            HumanMessagePromptTemplate.from_template(
                "answer the users question as best as possible.\n{format_instructions}\n{question}"
            )
        ],
        input_variables=["question"],
        partial_variables={"format_instructions": format_instructions},
    )

    _input = prompt.format_prompt(question="what's the capital of france")
    output = chat_model(_input.to_messages())

    output_obj = output_parser.parse(output.content)

    print(output_obj)


if __name__ == "__main__":
    main()
