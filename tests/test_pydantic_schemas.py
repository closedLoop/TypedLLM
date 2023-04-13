import unittest

from pydantic import BaseModel, Field

from typedllm.pydantic_schema import generate_json_schema


class TestPydanticShemas(unittest.TestCase):
    def test_convert_basemodel(self):
        """A Simple model should be converted to a flattened json schema"""

        class ExampleModel(BaseModel):
            name: str = Field(..., description="Name of the user")
            age: int | None = Field(..., description="Age of the user")

        json_schema = generate_json_schema(ExampleModel)
        self.assertDictEqual(
            json_schema,
            {
                "title": "ExampleModel",
                "type": "object",
                "properties": {
                    "name": {
                        "title": "Name",
                        "description": "Name of the user",
                        "type": "string",
                    },
                    "age": {
                        "title": "Age",
                        "description": "Age of the user",
                        "type": "integer",
                    },
                },
                "required": ["name", "age"],
            },
        )
