# Advanced Features of PHLang

Ang PHLang ay nagbibigay ng maraming advanced na feature upang mas maging versatile at kapaki-pakinabang para sa mga developer. Sa dokumentong ito, tatalakayin natin ang mga advanced na feature na ito at kung paano sila gamitin nang epektibo.

## 1. Error Handling

Ang PHLang ay mayroong komprehensibong sistema ng paghawak ng error na nakatutulong sa mga developer na mahanap at ma-debug ang mga problema sa kanilang code.

### Example:
```ph
subukan {
    x = 10 / 0  // Maghahagis ng error dahil hindi maaaring maghati sa zero
} saluhin (error) {
    idikta "Error: " + error
}
```

## 2. Function Overloading

Sa PHLang, maaari kang magbigay ng maraming implementation ng isang function na may iba-ibang parameter types:

### Example:
```ph
paraan magdagdag(a, b) {
    bumalik a + b
}

// Gamitin ang function para sa iba't ibang uri ng data
resulta1 = magdagdag(5, 3)       // 8
resulta2 = magdagdag("Hello", " World")  // "Hello World"
```

## 3. Nested Functions

Maaari kang magdeklara ng function sa loob ng isa pang function para sa mas mahusay na encapsulation:

### Example:
```ph
paraan outer() {
    x = 10
    
    paraan inner() {
        bumalik x * 2
    }
    
    bumalik inner()
}

resulta = outer()  // 20
```

## 4. Recursion

Ang PHLang ay sumusuporta sa recursion, na nagbibigay-daan sa isang function na tawagin ang sarili nito:

### Example:
```ph
paraan factorial(n) {
    kung n <= 1 {
        bumalik 1
    }
    bumalik n * factorial(n - 1)
}

idikta factorial(5)  // 120
```

## 5. Closures

Ang mga function sa PHLang ay maaaring maging closures, na nagtutulot sa kanila na i-access at panatilihin ang scope ng kanilang mga nakapalibot na variable:

### Example:
```ph
paraan counter() {
    count = 0
    
    paraan increment() {
        count = count + 1
        bumalik count
    }
    
    bumalik increment
}

myCounter = counter()
idikta myCounter()  // 1
idikta myCounter()  // 2
idikta myCounter()  // 3
```

## 6. Advanced Control Flow

PHLang ay nagbibigay ng advanced control flow statements katulad ng short-circuit evaluation:

### Example:
```ph
// Short-circuit evaluation
x = 5
y = 10
kung x > 0 and y > 0 {
    idikta "Parehong positibo"
}

// Ternary-style conditional
edad = 20
status = (edad >= 18) ? "adult" : "minor"
idikta status  // "adult"
```

## 7. String Manipulation

### Example:
```ph
pangalan = "Juan Dela Cruz"

// String concatenation
buongPangalan = "Mr. " + pangalan
idikta buongPangalan  // "Mr. Juan Dela Cruz"

// String length
haba = pangalan.length()
idikta "Ang haba ng pangalan ay " + haba
```

## 8. Working with Collections

### Example:
```ph
// Array
mga_numero = [1, 2, 3, 4, 5]
idikta mga_numero[0]  // 1

// Iterating over arrays
para (numero in mga_numero) {
    idikta numero
}

// Dictionary/Map
tao = {
    "pangalan": "Juan",
    "edad": 30,
    "trabaho": "Programmer"
}

idikta tao["pangalan"]  // "Juan"
```

## 9. File Operations

### Example:
```ph
// Reading a file
paraan basahin_file(filename) {
    subukan {
        content = file.read(filename)
        bumalik content
    } saluhin (error) {
        idikta "Hindi mabasa ang file: " + error
        bumalik wala
    }
}

// Writing to a file
paraan isulat_file(filename, content) {
    subukan {
        file.write(filename, content)
        bumalik tama
    } saluhin (error) {
        idikta "Hindi maisulat ang file: " + error
        bumalik mali
    }
}
```

## 10. Interoperability with Python

Ang PHLang ay maaaring makipag-ugnayan sa mga Python library, na nagbibigay-daan sa mga developer na gamitin ang malawak na ecosystem ng Python:

### Example:
```ph
// Paggamit ng Python library
paraan gamitin_python_lib() {
    math = python.import("math")
    idikta "Pi value: " + math.pi
    idikta "Square root of 16: " + math.sqrt(16)
}
```

## Konklusyon

Ang mga advanced na feature na ito ay nagbibigay sa PHLang ng malakas na capability na hindi lamang para sa mga basic programming task, kundi pati na rin para sa mga advanced na proyekto. Sa pamamagitan ng paggamit ng mga feature na ito, maaari kang bumuo ng mas mahusay, mas modular, at mas maintainable na code sa PHLang.