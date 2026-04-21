javascript
// Taschenrechner JavaScript

function add(a, b) {
    return a + b;
}

function subtract(a, b) {
    return a - b;
}

function multiply(a, b) {
    return a * b;
}

function divide(a, b) {
    if (b === 0) {
        return "Error: Division by zero";
    }
    return a / b;
}

function calculate(operation, num1, num2) {
    switch (operation) {
        case '+':
            return add(num1, num2);
        case '-':
            return subtract(num1, num2);
        case '*':
            return multiply(num1, num2);
        case '/':
            return divide(num1, num2);
        default:
            return "Invalid operation";
    }
}

// Beispielaufruf
console.log(calculate('+', 5, 3)); // Output: 8
console.log(calculate('-', 10, 4)); // Output: 6
console.log(calculate('*', 7, 2)); // Output: 14
console.log(calculate('/', 9, 3)); // Output: 3
console.log(calculate('%', 10, 3)); // Output: Error: Division by zero