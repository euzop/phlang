# PHLang Compiler

PHLang (Philippine Language) is a programming language designed to make coding more accessible to Filipino speakers by using Filipino keywords and natural syntax while maintaining the power of modern programming languages. It serves as a bridge between natural Filipino language and computer programming, enabling Filipino developers to write code in their native language.

## Features

- **Filipino Keywords**: Uses Filipino terms like `kung` (if), `habang` (while), and `idikta` (print)
- **Natural Syntax**: Designed to feel intuitive for native Filipino speakers
- **Full Functionality**: Supports all essential programming features including:
  - Variables and data types
  - Control structures (conditionals, loops)
  - Functions
  - Error handling
- **Lexical Analysis**: Breaks down source code into tokens
- **Parsing**: Ensures tokens follow the correct syntax
- **Semantic Analysis**: Validates data types and scopes
- **Code Generation**: Translates PHLang code to Python for execution
- **Error Handling**: Provides clear error messages in Filipino

## Example Code

```ph
// Hello World program in PHLang
idikta "Kumusta, Mundo!"

// Variables
pangalan = "Juan"
edad = 25

// Conditional statements
kung edad >= 18 {
    idikta pangalan + " ay nasa hustong gulang na."
} edi {
    idikta pangalan + " ay menor de edad pa."
}

// Functions
paraan magdagdag(a, b) {
    bumalik a + b
}

resulta = magdagdag(5, 3)
idikta "Ang resulta ay: " + resulta
```

## Getting Started

To get started with the PHLang compiler, follow these steps:

1. **Clone the Repository**:
   ```
   git clone https://github.com/euzop/phlang-compiler.git
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

- Language Specification: Detailed syntax and semantics of PHLang
- Compiler Design: Technical architecture of the compiler
- Getting Started Tutorial: Quick introduction to coding in PHLang
- Advanced Features Tutorial: Explore more complex capabilities

## Why PHLang?

PHLang makes programming more accessible to Filipino developers by:
- Reducing the language barrier for non-English speakers
- Making code more intuitive and readable for Filipino developers
- Serving as an educational tool for teaching programming concepts
- Preserving cultural identity in technological contexts

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.
