# Getting Started with PHLang Compiler

Welcome to the PHLang Compiler! This tutorial will guide you through the steps to get started with using the PHLang compiler for your custom programming language projects.

## Prerequisites

Before you begin, ensure you have the following installed on your system:

- Python 3.7 or higher
- pip (Python package installer)

## Installation

1. **Clone the Repository**

   First, clone the PHLang compiler repository from GitHub:

   ```
   git clone https://github.com/yourusername/phlang-compiler.git
   ```

2. **Navigate to the Project Directory**

   Change your working directory to the cloned repository:

   ```
   cd phlang-compiler
   ```

3. **Install Dependencies**

   Install the required dependencies using pip:

   ```
   pip install -r requirements.txt
   ```

## Compiling Your First PHLang Program

1. **Create a PHLang Source File**

   Create a new file with a `.ph` extension. For example, `hello.ph`:

   ```ph
   idikta "Kumusta, PHLang!"
   ```

2. **Compile and Run the Source File**

   Use the PHLang compiler to compile and run your source file. Run the following command in your terminal:

   ```
   python scripts/phlang.py examples/hello.ph
   ```

   This command will compile and execute your PHLang code, displaying the output in the terminal.

## Basic Syntax Examples

Here are some basic examples to get you started with PHLang:

### Variables and Data Types

```ph
pangalan = "Juan"
edad = 25
temperatura = 36.5
aktibo = tama
```

### Conditional Statements

```ph
kung edad >= 18 {
    idikta "Ikaw ay nasa hustong gulang na"
} kundi edad >= 13 {
    idikta "Ikaw ay teenager"
} edi {
    idikta "Ikaw ay bata pa"
}
```

### Loops

```ph
// While loop
x = 1
habang x <= 5 {
    idikta x
    x = x + 1
}

// For loop
para i = 0; i < 5; i = i + 1 {
    idikta "Bilang: " + i
}
```

### Functions

```ph
paraan magdagdag(a, b) {
    bumalik a + b
}

resulta = magdagdag(5, 3)
idikta "Ang resulta ay: " + resulta
```

### Error Handling

```ph
subukan {
    x = 10 / 0
    idikta x
} saluhin (error) {
    idikta "May error: Hindi maaaring maghati sa zero"
}
```

## Exploring Features

PHLang supports various features such as:

- Basic arithmetic operations (`+`, `-`, `*`, `/`, `%`)
- Comparison operators (`==`, `!=`, `<`, `>`, `<=`, `>=`)
- Logical operators (`and`, `or`, `not`)
- Control structures (`kung`, `kundi`, `edi`, `habang`, `para`)
- Functions (`paraan`)
- Error handling (`subukan`, `saluhin`)

Refer to the `docs/language_spec.md` for a complete list of features and syntax rules.

## Editor Tips

For a better development experience, you can use the PHLang IDE or configure your text editor to recognize PHLang files:

- Use `.ph` file extension for all PHLang source files
- Configure syntax highlighting for keywords like `kung`, `habang`, `paraan`, etc.
- If using VS Code, you can create a custom language configuration

## Common Issues and Solutions

- **Error: 'module' object has no attribute...**: Make sure you have installed all the required dependencies
- **Syntax errors**: Check the language specification for correct syntax
- **Runtime errors**: Use the `subukan`/`saluhin` blocks to handle potential errors

## Getting Help

If you encounter any issues or have questions, feel free to check the `README.md` for troubleshooting tips or reach out to the community on our GitHub page.

Happy coding with PHLang!