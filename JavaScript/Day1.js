
// ============================================================
// DELL UDAAN - JAVASCRIPT DAY 1
// Beginner Learning Notes + Programs
// ============================================================


// ============================================================
// TOPIC 1: INTRODUCTION TO JAVASCRIPT
// ============================================================

// DEFINITION:
// JavaScript is a programming language used to make websites
// interactive and dynamic. It can also be used outside browsers
// with environments such as Node.js.
//
// IMPORTANT CONCEPT:
// console.log() is used to display information in the console.
//
// SYNTAX:
// console.log(value);


// EXAMPLE:

console.log("Hello World!");
console.log("Welcome to JavaScript");
console.log(100);


// ============================================================
// TOPIC 2: RUNNING JAVASCRIPT
// ============================================================

// DEFINITION:
// JavaScript code can be executed using a browser console
// or a JavaScript runtime such as Node.js.
//
// IMPORTANT CONCEPTS:
// 1. Browser Console - runs JavaScript directly in the browser.
// 2. Node.js - runs JavaScript outside the browser.
// 3. console.log() - displays output.
//
// To run this file using Node.js:
// node Day1.js


// ============================================================
// TOPIC 3: VARIABLES
// ============================================================

// DEFINITION:
// A variable is a named storage location used to store
// information that can be accessed and used in a program.
//
// IMPORTANT CONCEPTS:
// 1. var  - older way of declaring variables.
// 2. let  - used when a value may change.
// 3. const - used when a variable should not be reassigned.
//
// ------------------------------------------------------------
// 3.1 LET
// ------------------------------------------------------------

// DEFINITION:
// let is used to declare a variable whose value can be changed.
//
// EXAMPLE:

{
    let age = 20;
    console.log("Age:", age);

    age = 21;
    console.log("Updated Age:", age);
}


// ------------------------------------------------------------
// 3.2 VAR
// ------------------------------------------------------------

// DEFINITION:
// var is the older keyword used to declare variables.
//
// IMPORTANT CONCEPT:
// var can be reassigned and redeclared.
// It has function scope rather than block scope.
//
// EXAMPLE:

{
    var studentName = "Rahul";
    console.log(studentName);

    studentName = "Amit";
    console.log(studentName);
}


// ------------------------------------------------------------
// 3.3 CONST
// ------------------------------------------------------------

// DEFINITION:
// const is used to declare variables that cannot be reassigned.
//
// IMPORTANT CONCEPT:
// Once a const variable is assigned, it cannot be reassigned.
//
// EXAMPLE:

{
    const collegeName = "SP College";
    console.log(collegeName);

    // collegeName = "ABC College"; // Error
}


// ------------------------------------------------------------
// VARIABLE NAMING RULES
// ------------------------------------------------------------

// 1. Variable names can contain letters, digits, _ and $.
// 2. Variable names cannot start with a digit.
// 3. Variable names are case-sensitive.
// 4. Reserved keywords cannot be used as variable names.
// 5. Use meaningful names.
//
// EXAMPLE:

{
    let firstName = "Madhura";
    let totalMarks = 90;

    console.log(firstName);
    console.log(totalMarks);
}


// ============================================================
// TOPIC 4: DATA TYPES
// ============================================================

// DEFINITION:
// A data type defines the kind of value stored in a variable.
//
// IMPORTANT CONCEPT:
// JavaScript is dynamically typed. A variable can hold values
// of different types during program execution.
//
// ------------------------------------------------------------
// 4.1 STRING
// ------------------------------------------------------------

// DEFINITION:
// A String represents text.
//
// Strings can be written using:
// 1. Double quotes
// 2. Single quotes
// 3. Backticks
//
// EXAMPLE:

{
    let student = "Rahul";
    let city = 'Pune';

    console.log(student);
    console.log(city);
}


// ------------------------------------------------------------
// 4.2 NUMBER
// ------------------------------------------------------------

// DEFINITION:
// Number represents numeric values, including integers
// and decimal numbers.
//
// EXAMPLE:

{
    let age = 20;
    let percentage = 85.5;

    console.log(age);
    console.log(percentage);
}


// ------------------------------------------------------------
// 4.3 BOOLEAN
// ------------------------------------------------------------

// DEFINITION:
// Boolean represents one of two values:
// true or false.
//
// IMPORTANT CONCEPT:
// Boolean values are commonly used in conditions.
//
// EXAMPLE:

{
    let isPassed = true;
    let hasSubmitted = false;

    console.log(isPassed);
    console.log(hasSubmitted);
}


// ------------------------------------------------------------
// 4.4 UNDEFINED
// ------------------------------------------------------------

// DEFINITION:
// Undefined means a variable has been declared
// but has not yet been assigned a value.
//
// EXAMPLE:

{
    let phoneNumber;

    console.log(phoneNumber); // undefined
}


// ------------------------------------------------------------
// 4.5 NULL
// ------------------------------------------------------------

// DEFINITION:
// Null represents an intentionally empty value.
//
// IMPORTANT CONCEPT:
// undefined generally means no value has been assigned.
// null is intentionally assigned to represent no value.
//
// EXAMPLE:

{
    let selectedCourse = null;

    console.log(selectedCourse);
}


// ------------------------------------------------------------
// 4.6 BIGINT
// ------------------------------------------------------------

// DEFINITION:
// BigInt is used to represent integers larger than the
// range safely supported by the normal Number type.
//
// IMPORTANT CONCEPT:
// BigInt values are written with n at the end.
//
// EXAMPLE:

{
    let largeNumber = 12345678901234567890n;

    console.log(largeNumber);
}


// ------------------------------------------------------------
// 4.7 SYMBOL
// ------------------------------------------------------------

// DEFINITION:
// Symbol creates a unique value that can be used as an identifier.
//
// IMPORTANT CONCEPT:
// Two Symbols with the same description are still different.
//
// EXAMPLE:

{
    let idA = Symbol("id");
    let idB = Symbol("id");

    console.log(idA === idB); // false
}


// ------------------------------------------------------------
// 4.8 CHECKING DATA TYPES USING TYPEOF
// ------------------------------------------------------------

// DEFINITION:
// typeof is an operator used to determine the data type
// of a value.
//
// EXAMPLE:

{
    let studentName = "Rahul";
    let studentAge = 20;
    let isPassed = true;

    console.log(typeof studentName); // string
    console.log(typeof studentAge); // number
    console.log(typeof isPassed);   // boolean
}


// ============================================================
// TOPIC 5: NON-PRIMITIVE DATA TYPES
// ============================================================

// IMPORTANT CONCEPT:
// Non-primitive data types can store collections of data
// or more complex structures.
//
// Common examples:
// 1. Array
// 2. Object
// 3. Function


// ------------------------------------------------------------
// 5.1 ARRAY
// ------------------------------------------------------------

// DEFINITION:
// An array stores multiple values in a single variable.
//
// IMPORTANT CONCEPTS:
// 1. Array values are stored in an ordered sequence.
// 2. Array indexing starts from 0.
// 3. Index 0 represents the first element.
//
// EXAMPLE:

{
    let fruits = ["Apple", "Mango", "Banana"];

    console.log(fruits);

    console.log(fruits[0]); // Apple
    console.log(fruits[1]); // Mango
    console.log(fruits[2]); // Banana

    // Invalid index example
    console.log(fruits[-2]); // undefined
}


// ------------------------------------------------------------
// 5.2 OBJECT
// ------------------------------------------------------------

// DEFINITION:
// An object stores related information in key-value pairs.
//
// IMPORTANT CONCEPTS:
// 1. Keys represent property names.
// 2. Values represent information associated with the keys.
// 3. Object properties can be accessed using dot notation.
//
// EXAMPLE:

{
    let student = {
        name: "Madhura",
        age: 20,
        course: "MCS"
    };

    console.log(student);

    console.log(student.name);
    console.log(student.age);
    console.log(student.course);

    // Adding a new property
    student.city = "Pune";

    console.log(student.city);
}


// ------------------------------------------------------------
// 5.3 FUNCTION
// ------------------------------------------------------------

// DEFINITION:
// A function is a reusable block of code designed
// to perform a particular task.
//
// Functions are explained in detail in Topic 10.


// ============================================================
// TOPIC 6: STRINGS AND STRING METHODS
// ============================================================

// DEFINITION:
// A string is a sequence of characters used to represent text.
//
// IMPORTANT CONCEPT:
// Strings are immutable in JavaScript.
// This means string methods normally return a new string
// instead of modifying the original string.

// ------------------------------------------------------------
// 6.1 STRING CONCATENATION
// ------------------------------------------------------------

// DEFINITION:
// Concatenation means joining two or more strings together.
//
// IMPORTANT CONCEPT:
// The + operator can be used to join strings.
//
// EXAMPLE:

{
    let firstName = "Rahul";
    let lastName = "Sharma";

    let fullName = firstName + " " + lastName;

    console.log(fullName);
}


// ------------------------------------------------------------
// 6.2 TEMPLATE LITERALS
// ------------------------------------------------------------

// DEFINITION:
// Template literals allow strings to contain variables
// and expressions.
//
// IMPORTANT CONCEPT:
// Template literals use backticks (`).
// Variables can be inserted using ${variable}.
//
// EXAMPLE:

{
    let name = "Rahul";
    let age = 20;

    console.log(`My name is ${name} and my age is ${age}.`);
}


// ------------------------------------------------------------
// 6.3 STRING LENGTH
// ------------------------------------------------------------

// DEFINITION:
// length returns the number of characters in a string.
//
// EXAMPLE:

{
    let language = "JavaScript";

    console.log(language.length);
}


// ------------------------------------------------------------
// 6.4 toUpperCase()
// ------------------------------------------------------------

// DEFINITION:
// Converts the string into uppercase letters.
//
// EXAMPLE:

{
    let text = "javascript";

    console.log(text.toUpperCase());
}


// ------------------------------------------------------------
// 6.5 toLowerCase()
// ------------------------------------------------------------

// DEFINITION:
// Converts the string into lowercase letters.
//
// EXAMPLE:

{
    let text = "JAVASCRIPT";

    console.log(text.toLowerCase());
}


// ------------------------------------------------------------
// 6.6 trim()
// ------------------------------------------------------------

// DEFINITION:
// Removes spaces from the beginning and end of a string.
//
// IMPORTANT CONCEPT:
// It does not remove spaces from the middle of a string.
//
// EXAMPLE:

{
    let text = "   Madhura   ";

    console.log(text.trim());
}


// ------------------------------------------------------------
// 6.7 includes()
// ------------------------------------------------------------

// DEFINITION:
// includes() checks whether a string contains
// a specified value.
//
// RETURN VALUE:
// true or false.
//
// EXAMPLE:

{
    let message = "I am learning JavaScript";

    console.log(message.includes("learning")); // true
    console.log(message.includes("Python"));  // false
}


// ------------------------------------------------------------
// 6.8 slice()
// ------------------------------------------------------------

// DEFINITION:
// slice() extracts a portion of a string.
//
// IMPORTANT CONCEPT:
// The ending index is not included.
// String indexing starts from 0.
//
// EXAMPLE:

{
    let language = "JavaScript";

    console.log(language.slice(0, 4)); // Java
}


// ============================================================
// TOPIC 7: OPERATORS
// ============================================================

// DEFINITION:
// Operators are symbols used to perform operations
// on variables and values.

// ------------------------------------------------------------
// 7.1 ARITHMETIC OPERATORS
// ------------------------------------------------------------

// DEFINITION:
// Arithmetic operators perform mathematical operations.
//
// OPERATORS:
// + Addition
// - Subtraction
// * Multiplication
// / Division
// % Modulus (remainder)
// ** Exponentiation
// ++ Increment
// -- Decrement

// EXAMPLE:

{
    let a = 10;
    let b = 5;

    console.log("Addition:", a + b);
    console.log("Subtraction:", a - b);
    console.log("Multiplication:", a * b);
    console.log("Division:", a / b);
    console.log("Modulus:", a % 3);
    console.log("Exponent:", 2 ** 3);

    let x = 4;

    x++;
    console.log("Increment:", x);

    x--;
    console.log("Decrement:", x);
}


// ------------------------------------------------------------
// 7.2 MODULUS OPERATOR
// ------------------------------------------------------------

// DEFINITION:
// The modulus (%) operator returns the remainder
// after division.
//
// IMPORTANT CONCEPT:
// It can be used to check whether a number is even or odd.
//
// EXAMPLE:

{
    let number = 10;

    console.log(number % 2); // 0

    if (number % 2 === 0) {
        console.log("Even Number");
    } else {
        console.log("Odd Number");
    }
}


// ------------------------------------------------------------
// 7.3 ASSIGNMENT OPERATORS
// ------------------------------------------------------------

// DEFINITION:
// Assignment operators assign values to variables.
//
// IMPORTANT CONCEPT:
// Compound assignment operators combine an operation
// with an assignment.
//
// OPERATORS:
// =   Assign
// +=  Add and assign
// -=  Subtract and assign
// *=  Multiply and assign
// /=  Divide and assign
//
// EXAMPLE:

{
    let x = 10;

    x += 5; // x = x + 5
    console.log(x);

    x -= 2; // x = x - 2
    console.log(x);

    x *= 2; // x = x * 2
    console.log(x);

    x /= 2; // x = x / 2
    console.log(x);
}


// ------------------------------------------------------------
// 7.4 COMPARISON OPERATORS
// ------------------------------------------------------------

// DEFINITION:
// Comparison operators compare two values
// and return a Boolean value (true or false).
//
// IMPORTANT CONCEPT:
// ==  compares values after possible type conversion.
// === compares values and data types.
//
// OPERATORS:
// ==  Equal
// === Strictly equal
// !=  Not equal
// !== Strictly not equal
// >   Greater than
// <   Less than
// >=  Greater than or equal to
// <=  Less than or equal to
//
// EXAMPLE:

{
    console.log(10 == "10");  // true
    console.log(10 === "10"); // false

    console.log(10 != 5);     // true
    console.log(10 !== "10"); // true

    console.log(10 > 5);      // true
    console.log(10 < 5);      // false

    console.log(10 >= 10);    // true
    console.log(10 <= 5);     // false
}


// IMPORTANT:
// Prefer === and !== in most beginner programs
// because they avoid unexpected type conversions.


// ------------------------------------------------------------
// 7.5 LOGICAL OPERATORS
// ------------------------------------------------------------

// DEFINITION:
// Logical operators combine or reverse conditions.
//
// OPERATORS:
// && (AND) - true if both conditions are true.
// || (OR)  - true if at least one condition is true.
// !  (NOT) - reverses a Boolean value.
//
// EXAMPLE:

{
    let age = 20;
    let hasID = true;

    console.log(age >= 18 && hasID === true);

    let hasEmail = false;
    let hasPhone = true;

    console.log(hasEmail || hasPhone);

    let isAbsent = false;

    console.log(!isAbsent);
}


// ------------------------------------------------------------
// 7.6 TERNARY OPERATOR
// ------------------------------------------------------------

// DEFINITION:
// The ternary operator is a short way to make
// a decision between two values.
//
// SYNTAX:
// condition ? value_if_true : value_if_false
//
// IMPORTANT CONCEPT:
// If the condition is true, the first value is selected.
// Otherwise, the second value is selected.
//
// EXAMPLE:

{
    let age = 20;

    let result = age >= 18
        ? "Eligible"
        : "Not Eligible";

    console.log(result);
}


// ============================================================
// TOPIC 8: SETS
// ============================================================

// DEFINITION:
// A Set is a collection that stores unique values.
//
// IMPORTANT CONCEPTS:
// 1. Duplicate values are not stored.
// 2. Sets preserve insertion order.
// 3. Sets do not provide index-based access like arrays.
// 4. Sets can be used to remove duplicate values.

// ------------------------------------------------------------
// 8.1 CREATING A SET
// ------------------------------------------------------------

{
    let fruits = new Set([
        "Apple",
        "Mango",
        "Apple",
        "Banana"
    ]);

    console.log(fruits);
}


// ------------------------------------------------------------
// 8.2 ADDING VALUES
// ------------------------------------------------------------

// DEFINITION:
// add() inserts a new value into a Set.
//
// IMPORTANT:
// Adding an existing value does not create a duplicate.

{
    let numbers = new Set();

    numbers.add(10);
    numbers.add(20);
    numbers.add(30);
    numbers.add(10);

    console.log(numbers);
}


// ------------------------------------------------------------
// 8.3 SET METHODS
// ------------------------------------------------------------

// add(value)    - adds a value
// delete(value) - removes a value
// has(value)    - checks whether a value exists
// size          - returns the number of unique values
// clear()       - removes all values

{
    let values = new Set([10, 20, 30]);

    values.add(40);

    console.log(values.has(20)); // true

    values.delete(10);

    console.log(values);
    console.log(values.size);

    // values.clear();
    // console.log(values);
}


// ============================================================
// TOPIC 9: CONTROL STRUCTURES
// ============================================================

// DEFINITION:
// Control structures determine the order in which
// instructions are executed.
//
// IMPORTANT CONCEPT:
// They allow programs to make decisions based on conditions.

// ------------------------------------------------------------
// 9.1 IF STATEMENT
// ------------------------------------------------------------

// DEFINITION:
// An if statement executes a block of code
// only when its condition is true.
//
// SYNTAX:
// if (condition) {
//     statements
// }
//
// EXAMPLE:

{
    let age = 20;

    if (age >= 18) {
        console.log("You are eligible to vote");
    }
}


// ------------------------------------------------------------
// 9.2 IF-ELSE STATEMENT
// ------------------------------------------------------------

// DEFINITION:
// if-else is used when a program must choose
// between two possible paths.
//
// IMPORTANT CONCEPT:
// if executes when the condition is true.
// else executes when the condition is false.
//
// EXAMPLE:

{
    let marks = 35;

    if (marks >= 40) {
        console.log("Pass");
    } else {
        console.log("Fail");
    }
}


// ------------------------------------------------------------
// 9.3 IF-ELSE-IF STATEMENT
// ------------------------------------------------------------

// DEFINITION:
// if-else-if is used when multiple conditions
// need to be checked.
//
// IMPORTANT CONCEPT:
// Conditions are checked from top to bottom.
// The first true condition executes.
//
// EXAMPLE:

{
    let marks = 85;

    if (marks >= 90) {
        console.log("Grade A+");
    } else if (marks >= 80) {
        console.log("Grade A");
    } else if (marks >= 60) {
        console.log("Grade B");
    } else if (marks >= 40) {
        console.log("Grade C");
    } else {
        console.log("Fail");
    }
}


// ------------------------------------------------------------
// 9.4 NESTED IF
// ------------------------------------------------------------

// DEFINITION:
// A nested if is an if statement placed inside
// another if statement.
//
// IMPORTANT CONCEPT:
// The inner condition is checked only when
// the outer condition is satisfied.
//
// EXAMPLE:

{
    let age = 20;
    let hasID = true;

    if (age >= 18) {

        if (hasID === true) {
            console.log("Entry Allowed");
        } else {
            console.log("ID Required");
        }

    } else {
        console.log("Not Allowed");
    }
}


// ------------------------------------------------------------
// 9.5 SWITCH STATEMENT
// ------------------------------------------------------------

// DEFINITION:
// A switch statement selects a block of code
// based on the value of an expression.
//
// IMPORTANT CONCEPTS:
// 1. case represents a possible value.
// 2. break stops execution of the switch.
// 3. default runs when no case matches.
// 4. switch uses strict matching.
//
// EXAMPLE:

{
    let choice = 3;

    switch (choice) {

        case 1:
            console.log("Admission");
            break;

        case 2:
            console.log("Fees");
            break;

        case 3:
            console.log("Courses");
            break;

        default:
            console.log("Invalid Choice");
    }
}


// ============================================================
// TOPIC 10: LOOPS
// ============================================================

// DEFINITION:
// A loop repeatedly executes a block of code.
//
// IMPORTANT CONCEPT:
// Loops help avoid writing the same code multiple times.

// ------------------------------------------------------------
// 10.1 FOR LOOP
// ------------------------------------------------------------

// DEFINITION:
// A for loop is commonly used when the number
// of repetitions is known.
//
// SYNTAX:
// for (initialization; condition; update) {
//     statements
// }
//
// IMPORTANT CONCEPTS:
// Initialization - starting value
// Condition     - decides whether loop continues
// Update       - changes the value after each iteration
//
// EXAMPLE:

{
    for (let i = 1; i <= 5; i++) {
        console.log(i);
    }
}


// ------------------------------------------------------------
// 10.2 WHILE LOOP
// ------------------------------------------------------------

// DEFINITION:
// A while loop repeats as long as its condition is true.
//
// IMPORTANT CONCEPT:
// The condition is checked before executing the code.
//
// EXAMPLE:

{
    let i = 1;

    while (i <= 5) {
        console.log(i);
        i++;
    }
}


// ------------------------------------------------------------
// 10.3 DO-WHILE LOOP
// ------------------------------------------------------------

// DEFINITION:
// A do-while loop executes the code first
// and checks the condition afterward.
//
// IMPORTANT CONCEPT:
// A do-while loop executes at least once,
// even if the condition is initially false.
//
// EXAMPLE:

{
    let i = 10;

    do {
        console.log(i);
        i++;
    } while (i <= 5);
}


// ------------------------------------------------------------
// 10.4 BREAK
// ------------------------------------------------------------

// DEFINITION:
// break terminates a loop immediately.
//
// IMPORTANT CONCEPT:
// Once break executes, the loop stops completely.
//
// EXAMPLE:

{
    for (let i = 1; i <= 10; i++) {

        if (i === 5) {
            break;
        }

        console.log(i);
    }
}


// ------------------------------------------------------------
// 10.5 CONTINUE
// ------------------------------------------------------------

// DEFINITION:
// continue skips the current iteration
// and moves to the next iteration.
//
// IMPORTANT CONCEPT:
// It does not terminate the entire loop.
//
// EXAMPLE:

{
    for (let i = 1; i <= 5; i++) {

        if (i === 3) {
            continue;
        }

        console.log(i);
    }
}


// ============================================================
// TOPIC 11: FUNCTIONS
// ============================================================

// DEFINITION:
// A function is a reusable block of code
// designed to perform a specific task.
//
// IMPORTANT CONCEPTS:
// 1. Functions reduce code repetition.
// 2. Functions help organize programs.
// 3. A function can accept inputs.
// 4. A function can return an output.
//
// ------------------------------------------------------------
// 11.1 FUNCTION DECLARATION
// ------------------------------------------------------------

// DEFINITION:
// A function declaration defines a function
// using the function keyword.
//
// IMPORTANT CONCEPT:
// Defining a function does not automatically execute it.
// The function must be called.
//
// EXAMPLE:

{
    function greet() {
        console.log("Hello Students");
    }

    greet();
}


// ------------------------------------------------------------
// 11.2 FUNCTION WITHOUT PARAMETERS
// ------------------------------------------------------------

// DEFINITION:
// A function without parameters does not
// receive input values from the caller.
//
// EXAMPLE:

{
    function welcome() {
        console.log("Welcome to JavaScript Class");
    }

    welcome();
}


// ------------------------------------------------------------
// 11.3 PARAMETERS AND ARGUMENTS
// ------------------------------------------------------------

// DEFINITION:
// Parameter:
// A variable written in the function definition.
//
// Argument:
// The actual value passed while calling the function.
//
// IMPORTANT CONCEPT:
// Parameters receive values from arguments.
//
// EXAMPLE:

{
    function greetStudent(name) {
        console.log("Hello " + name);
    }

    greetStudent("Rahul");
    greetStudent("Amit");
}


// ------------------------------------------------------------
// 11.4 MULTIPLE PARAMETERS
// ------------------------------------------------------------

// DEFINITION:
// A function can accept multiple parameters
// to perform operations using multiple values.
//
// EXAMPLE:

{
    function add(a, b) {
        console.log(a + b);
    }

    add(10, 20);
    add(50, 30);
}


// ------------------------------------------------------------
// 11.5 RETURN STATEMENT
// ------------------------------------------------------------

// DEFINITION:
// return sends a value from a function
// back to the place where it was called.
//
// IMPORTANT CONCEPT:
// console.log() displays a value.
// return gives a value back for further use.
//
// EXAMPLE:

{
    function addition(a, b) {
        return a + b;
    }

    let result = addition(10, 20);

    console.log(result);
}


// ------------------------------------------------------------
// 11.6 FUNCTION WITH CONDITION
// ------------------------------------------------------------

// IMPORTANT CONCEPT:
// A function can contain conditional statements
// and return different values based on conditions.
//
// EXAMPLE:

{
    function checkResult(marks) {

        if (marks >= 40) {
            return "Pass";
        } else {
            return "Fail";
        }

    }

    console.log(checkResult(75));
    console.log(checkResult(30));
}


// ------------------------------------------------------------
// 11.7 ARROW FUNCTIONS
// ------------------------------------------------------------

// DEFINITION:
// An arrow function is a shorter way to write
// a function expression.
//
// IMPORTANT CONCEPT:
// Arrow functions use the => symbol.
//
// EXAMPLE:

{
    const add = (a, b) => {
        return a + b;
    };

    console.log(add(10, 20));
}


// ------------------------------------------------------------
// 11.8 IMPLICIT RETURN IN ARROW FUNCTIONS
// ------------------------------------------------------------

// IMPORTANT CONCEPT:
// If an arrow function contains only one expression,
// curly braces and return can be omitted.
//
// EXAMPLE:

{
    const multiply = (a, b) => a * b;

    console.log(multiply(4, 5));
}


// ============================================================
// TOPIC 12: PRACTICE PROGRAM
// CALCULATE TOTAL AND AVERAGE OF THREE SUBJECTS
// ============================================================

// QUESTION:
// Create a function named calculateResult().
// It should accept marks of three subjects.
//
// Calculate:
// 1. Total marks
// 2. Average marks
//
// Return both values and display them.
//
// IMPORTANT CONCEPTS USED:
// 1. Function
// 2. Parameters
// 3. Arithmetic operators
// 4. Return
// 5. Object
//
// PROGRAM:

{
    function calculateResult(sub1, sub2, sub3) {

        let total = sub1 + sub2 + sub3;
        let average = total / 3;

        return {
            total: total,
            average: average
        };
    }

    let result = calculateResult(80, 70, 90);

    console.log("Total Marks:", result.total);
    console.log("Average Marks:", result.average);
}


// ============================================================
// END OF DAY 1 JAVASCRIPT NOTES
// ============================================================
