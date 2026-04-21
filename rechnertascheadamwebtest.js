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
        case 'add':
            return add(num1, num2);
        case'subtract':
            return subtract(num1, num2);
        case'multiply':
            return multiply(num1, num2);
        case 'divide':
            return divide(num1, num2);
        default:
            return "Invalid operation";
    }
}

// Testen des Taschenrechners
console.log(calculate('add', 5, 3)); // Output: 8
console.log(calculate('subtract', 10, 4)); // Output: 6
console.log(calculate('multiply', 7, 6)); // Output: 42
console.log(calculate('divide', 9, 3)); // Output: 3
console.log(calculate('divide', 10, 0)); // Output: Error: Division by zero
console.log(calculate('invalid', 5, 3)); // Output: Invalid operation