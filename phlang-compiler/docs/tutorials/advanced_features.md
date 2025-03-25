# Advanced Features of PHLang

Ang PHLang ay nagbibigay ng maraming advanced na feature upang mas maging versatile at kapaki-pakinabang para sa mga developer. Sa dokumentong ito, tatalakayin natin ang mga advanced na feature na ito at kung paano sila gamitin nang epektibo.

## 1. Error Handling

Ang PHLang ay mayroong komprehensibong sistema ng paghawak ng error na nakatutulong sa mga developer na mahanap at ma-debug ang mga problema sa kanilang code.

### Example:
```ph
subukan {
    x = 10 / 0  // Maghahagis ng error dahil hindi maaaring maghati sa zero
} saluhin (error) {
    idikta "Error: " + error  // Output: Error: HindiMaaringHatiin: division by zero
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

idikta resulta1
idikta resulta2
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

resulta = outer()
idikta resulta
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
// Simple function that returns a value
paraan counter(start) {
    bumalik start + 5
}

// Multiple calls
idikta counter(5)   // 10
idikta counter(10)  // 15
idikta counter(15)  // 20
```

## 6. Advanced Control Flow

PHLang ay nagbibigay ng advanced control flow statements katulad ng short-circuit evaluation:

### Example:
```ph
// Short-circuit evaluation
x = 5
y = 10
kung x > 0 at y > 0 {
    idikta "Parehong positibo"
}

edad = 20  
kung edad >= 18 {
    status = "adult"
} edi {
    status = "minor"
}
idikta status  
```

## 7. String Manipulation

### Example:
```ph
pangalan = "Juan Dela Cruz"

// String concatenation
buongPangalan = "Mr. " + pangalan
idikta buongPangalan  // "Mr. Juan Dela Cruz"

// String length calculation
haba = 0
para i sa saklaw(14) {  // Length of "Juan Dela Cruz"
    haba = haba + 1
}
// Convert to string explicitly
idikta "Ang haba ng pangalan ay " + str(haba)
```

## 8. Working with Collections

### Example:
```ph
// Array literals
mga_numero = [1, 2, 3, 4, 5]
idikta mga_numero[0]  // 1

// Iterating over arrays
para i sa saklaw(5) {
    idikta mga_numero[i]
}

// Simple key-value pairs
pangalan = "Juan"
edad = 30
trabaho = "Programmer"

idikta "Pangalan: " + pangalan
idikta "Edad: " + edad
idikta "Trabaho: " + trabaho
```

## 9. Loops with Range

PHLang supports Filipino-style for loops with range:

### Example:
```ph
// Basic for loop with range
para i sa saklaw(5) {
    idikta i  // Outputs: 0, 1, 2, 3, 4
}

// For loop with running sum
x = 0
para i sa saklaw(10) {
    x = x + i
    idikta x  // Outputs: 0, 1, 3, 6, 10, 15, 21, 28, 36, 45
}
```

## 10. Logical Operators

PHLang uses Filipino logical operators:

### Example:
```ph
a = 5
b = 10

// Logical AND
kung a > 0 at b > 0 {
    idikta "Pareho silang positibo"
}

// Logical OR
kung a < 0 o b > 0 {
    idikta "Isa sa kanila ay tumutugon sa kondisyon"
}

// Logical NOT
kung hindi (a > b) {
    idikta "Hindi mas malaki ang a kaysa b"
}
```

## 11. Simple Input/Output

PHLang provides basic I/O operations:

### Example:
```ph
// Output
idikta "Ano ang pangalan mo?"

// For input, you would typically use a built-in function
// Not showing implementation details as this depends on your specific I/O design
pangalan = "Juan"  // This would be from input
idikta "Kumusta, " + pangalan + "!"
```

## Konklusyon

Ang mga advanced na feature na ito ay nagbibigay sa PHLang ng malakas na capability na hindi lamang para sa mga basic programming task, kundi pati na rin para sa mga advanced na proyekto. Sa pamamagitan ng paggamit ng mga feature na ito, maaari kang bumuo ng mas mahusay, mas modular, at mas maintainable na code sa PHLang.