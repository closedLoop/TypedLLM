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
To install TypedLLM, follow these steps:

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
    Install the required packages:
    ```
    pip install -r requirements.txt
    ```

## Usage
To use TypedLLM, first import the necessary modules:

```python
from typedllm import TypedLLM, PydanticConverter
```

Then, create an instance of the converter and process your text output:

```python
converter = PydanticConverter()
typed_output = converter.convert(text_output)
```

For more detailed examples, please refer to the examples directory.

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


## Testing

To run tests for TypedLLM, follow these steps:

Install the required testing packages:
```
pip install -r requirements-dev.txt
```
Run the tests:
```
pytest
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
