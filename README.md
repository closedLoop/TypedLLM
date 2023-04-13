# TypedLLM: Large Language Model to Typed Dataclass Conversion

TypedLLM is a Python repository that streamlines the process of converting unstructured text outputs from large language models into strongly typed dataclasses, like Pydantic, facilitating seamless integration with applications and enhancing data handling for improved consistency and maintainability.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [API Documentation](#api-documentation)
- [Contributing](#contributing)
- [Testing](#testing)
- [License](#license)
- [Credits/Acknowledgements](#creditsacknowledgements)
- [Changelog](#changelog)
- [Contact Information](#contact-information)

## Installation
To install TypedLLM, follow one of these options:

It is recommended to install TypedLLM in a virtual environment. To do so, follow these steps:

    python3 -m venv venv
    source venv/bin/activate
    # or do similar if you are using poetry or conda to manage your virtual environment

1. Pip install.
    ```
    pip install typedllm
    ```

2. Clone the repository:
    ```
    git clone https://github.com/username/TypedLLM.git
    ```
    Change to the project directory:
    ```
    cd TypedLLM
    ```
    Install the dependencies and the library
    ```
    pip install -r requirements.txt
    pip install .
    ```

## Usage
To use TypedLLM, first import the necessary modules:

    ```python
    from pydantic import Field, BaseModel
    from typedllm.pytandic_schema import typedllm_call

    task = "Brainstorm a json list of 10 examples of ExampleModel instances."
    # task = "What is the personal information of Barack Obama?"
    llm = OpenAI(temperature=0)


    class ExampleModel(BaseModel):
        name: str = Field(..., description="Name of the user")
        age: int = Field(..., description="Age of the user")


    data = typedllm_call(task, llm, ExampleModel)
    print(data)
    ```
Outputs
    ```
    [ExampleModel(name='John Doe', age=25), ExampleModel(name='Jane Doe', age=22), ExampleModel(name='Bob Smith', age=30), ExampleModel(name='Alice Smith', age=28), ExampleModel(name='Johnathan Johnson', age=32), ExampleModel(name='Jill Johnson', age=27), ExampleModel(name='James Williams', age=35), ExampleModel(name='Sarah Williams', age=33), ExampleModel(name='David Brown', age=40), ExampleModel(name='Emily Brown', age=38)]```


## Configuration
No specific configuration is required to use TypedLLM. However, you can customize the behavior of the converter by extending the PydanticConverter class and overriding its methods, if needed.

## API Documentation
Please refer to the API documentation for a complete list of available functions, classes, methods, and parameters.

## Contributing
We welcome contributions to TypedLLM! To contribute, please follow these guidelines:

1. Fork the repository and create your branch from the main branch.
1. Make your changes, ensuring you follow the project's coding style and documentation standards.
1. Submit a pull request with a clear description of your changes.

### Development Environment

Set up a virtual environment:

    python3 -m venv venv
    source venv/bin/activate

    # install dependencies
    pip install -r requirements.txt
    pip install -r requirements-dev.txt

    # install typedllm
    pip install -e .

    # Install pre-commit hooks
    pre-commit install


## Testing

To run tests for TypedLLM, follow these steps:

Install the required testing packages:
```
pip install -r requirements-dev.txt
```
Run the tests one of three ways:
```
pytest
# or
python tests/all.py
# or run
./run_tests_with_coverage.sh
```

## License
TypedLLM is released under the [MIT License](LICENSE).

## Credits/Acknowledgements
We would like to thank the following libraries and resources that have been instrumental in the development of TypedLLM:

 * Pydantic: https://github.com/pydantic/pydantic
 * LangChain: https://python.langchain.com/

## Changelog
Please refer to the [CHANGELOG.md](CHANGELOG.md) file for a summary of notable changes in each release of TypedLLM.

## Contact Information
For any questions or suggestions, please reach out to the TypedLLM maintainers:

* Email: [sean@closedloop.tech](mailto:sean@closedloop.tech)
* Twitter: [@seankruzel](https://twitter.com/seankruzel)
* GitHub Issues: https://github.com/closedloop/TypedLLM/issues
