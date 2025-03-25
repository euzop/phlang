# PHLang Language Specification

## Pangkalahatang-ideya
Ang PHLang ay isang programming language na idinisenyo para sa simplicity at ease of use, na ginagamit ang Filipino keywords habang nagbibigay ng powerful features para sa mga Filipino developers.

## Mga Syntax Rules

### Pangunahing Istraktura
Ang isang PHLang program ay binubuo ng mga statements. Pwedeng maglagay ng semicolon (`;`) sa dulo ng statement pero opsyonal ito. 

```ph
x = 10
idikta "Hello World"
```

### Mga Komento
Sinusuportahan ng PHLang ang C-style comments:
- Single-line comments gamit ang 
- Multi-line comments sa pagitan ng `/*` at `*/`

```ph
// Ito ay single-line comment

/*
Ito ay multi-line comment
na tumatagal ng maraming linya
*/
```

### Mga Uri ng Data
Sinusuportahan ng PHLang ang mga sumusunod na data types:
- Numbers (integers at floating-point): `42`, `3.14`
- Strings (nakalagay sa single o double quotes): `"Hello"`, `'World'`
- Boolean: `tama` (true) o `mali` (false)
- Null value: `wala`

### Mga Variable
Ang mga variable ay pwedeng gamitin nang direkta (hindi kinakailangang i-deklara):

```ph
pangalan = "Juan"
edad = 25
```

### Mga Control Structure

#### Conditional Statements
```ph
kung edad >= 18 {
    idikta "Ikaw ay nasa hustong gulang na"
} kundi edad >= 13 {
    idikta "Ikaw ay teenager"
} edi {
    idikta "Ikaw ay bata pa"
}
```

#### Loops

##### While Loop
```ph
habang kondisyon {
    // code na uulitin habang tama ang kondisyon
}
```

Halimbawa:
```ph
x = 1
habang x <= 5 {
    idikta x
    x = x + 1
}
```

##### For Loop
```ph
para i = 0; i < 10; i = i + 1 {
    idikta i
}
```

##### Loop Control
```ph
itigil     // tapusin ang loop
ituloy     // laktawan ang natitirang code at magpatuloy sa susunod na iteration
```

### Mga Function
Functions ay idinedeklara gamit ang `paraan` keyword:

```ph
paraan magdagdag(a, b) {
    bumalik a + b
}

// Pagtawag sa function
resulta = magdagdag(5, 3)
idikta resulta
```

### Paghawak ng Error
```ph
subukan {
    // code na maaaring mag-error
    x = 10 / 0
} saluhin (error) {
    // code para sa error handling
    idikta "May error: Hindi pwedeng maghati sa zero"
}
```

### Output
Gamit ang `idikta` para sa pag-output:

```ph
idikta "Hello World"        // walang parentheses
idikta("Hello " + "World")  // may parentheses
```

## Mga Operator

### Arithmetic Operators
- `+` (pagdagdag)
- `-` (pagbawas)
- `*` (pagmultiplika)
- `/` (paghati)
- `%` (modulo/remainder)

### Comparison Operators
- `==` (equal)
- `!=` (not equal)
- `<` (less than)
- `>` (greater than)
- `<=` (less than or equal)
- `>=` (greater than or equal)

### Logical Operators
- `and` (logical AND)
- `or` (logical OR)
- `not` (logical NOT)

## Mga Reserved Keyword
Ang mga sumusunod na mga keyword ay nakalaan at hindi maaaring gamitin bilang mga identifier:

| Keyword | English Equivalent | Paggamit |
|---------|-------------------|----------|
| `kung` | if | Conditional statement |
| `kundi` | else if | Secondary conditional |
| `edi` | else | Default branch |
| `habang` | while | While loop |
| `para` | for | For loop |
| `paraan` | function/def | Function definition |
| `bumalik` | return | Return value |
| `itigil` | break | Exit a loop |
| `ituloy` | continue | Skip to next iteration |
| `idikta` | print | Display output |
| `subukan` | try | Begin error handling |
| `saluhin` | except/catch | Handle exceptions |
| `tama` | true | Boolean true value |
| `mali` | false | Boolean false value |
| `wala` | none/null | Null value |

## Mga Halimbawa ng Program

### Hello World
```ph
idikta "Kumusta, Mundo!"
```

### Calculator
```ph
paraan simula() {
    a = 10
    b = 5
    
    idikta "Addition: " + (a + b)
    idikta "Subtraction: " + (a - b)
    idikta "Multiplication: " + (a * b)
    idikta "Division: " + (a / b)
}

simula()
```

### Factorial
```ph
paraan factorial(n) {
    kung n <= 1 {
        bumalik 1
    }
    bumalik n * factorial(n - 1)
}

paraan simula() {
    num = 5
    idikta "Factorial ng " + num + " ay " + factorial(num)
}

simula()
```

### Conditional Example
```ph
x = 11
kung x > 10 {
    idikta "Hello"
} kundi x == 5 {
    idikta "World"
} edi {
    idikta "Yo"
}
```

### Loop Example
```ph
// While loop
bilang = 1
habang bilang <= 5 {
    idikta bilang
    bilang = bilang + 1
}

// For loop
para i = 0; i < 5; i = i + 1 {
    kung i == 2 {
        ituloy  // Skip sa number 2
    }
    idikta "Counter: " + i
}
```

### Error Handling
```ph
subukan {
    x = 10 / 0
    idikta x
} saluhin (error) {
    idikta "Error: Hindi pwedeng maghati sa zero"
}
```

## Konklusyon
Ang PHLang ay isang programming language na nagbibigay-daan sa mga Filipino na mag-code gamit ang mga pamilyar na salita sa Filipino. Ito ay ginagawang mas accessible ang programming para sa mga baguhan sa programming at nagbibigay ng natural na paraan ng pagpapahayag ng logic para sa mga native Filipino speakers. Para sa karagdagang detalye, sumangguni sa documentation ng compiler at mga halimbawang program sa repository.