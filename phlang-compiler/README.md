# PHLang Compiler

PHLang is a custom programming language designed for educational purposes, focusing on simplicity and ease of use. This project includes a complete compiler for PHLang, featuring lexical analysis, parsing, semantic analysis, code generation, and error handling.

## Features

- **Lexical Analysis**: Breaks down source code into tokens.
- **Parsing**: Ensures tokens follow the correct syntax.
- **Semantic Analysis**: Validates data types and scopes.
- **Code Generation**: Translates the Abstract Syntax Tree (AST) into executable code.
- **Error Handling**: Provides clear error messages for syntax and semantic errors.

## Getting Started

To get started with the PHLang compiler, follow these steps:

1. **Clone the Repository**:
   ```
   git clone https://github.com/yourusername/phlang-compiler.git
   cd phlang-compiler
   ```

2. **Install Dependencies**:
   ```
   pip install -r requirements.txt
   ```

3. **Run the Compiler**:
   You can compile a PHLang file using the following command:
   ```
   python scripts/phlang.py examples/hello_world.ph
   ```

## Documentation

For detailed documentation, including language specifications and tutorials, please refer to the `docs` directory.

- [Language Specification](docs/language_spec.md)
- [Compiler Design](docs/compiler_design.md)
- [Getting Started Tutorial](docs/tutorials/getting_started.md)
- [Advanced Features Tutorial](docs/tutorials/advanced_features.md)

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.