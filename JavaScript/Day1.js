
/*
=====================================================
          DELL UDAAN - JAVASCRIPT DAY 1
          Beginner Student Practice
=====================================================
*/

// ===================================================
// 1. INTRODUCTION TO JAVASCRIPT
// ===================================================

// console.log() is used to display output.

console.log("Hello World!");
console.log("Welcome to JavaScript");
console.log(100);


// ===================================================
// 2. VARIABLES: var, let and const
// ===================================================

// 1. let - value can be changed

let age = 20;
console.log("Age:", age);

age = 21;
console.log("Updated Age:", age);


// 2. var - older way of declaring variables

var studentName = "Rahul";
console.log(studentName);

studentName = "Amit";
console.log(studentName);


// 3. const - value cannot be reassigned

const collegeName = "SP College";
console.log(collegeName);

// const collegeName = "ABC"; // Error


// Variable naming examples

let firstName = "Madhura";
let totalMarks = 90;

console.log(firstName);
console.log(totalMarks);


// ===================================================
// 3. DATA TYPES
// ===================================================

// 1. String

let name = "Madhura";
let city = "Pune";

console.log(name);
console.log(city);


// 2. Number

let studentAge = 20;
let percentage = 85.5;

console.log(studentAge);
console.log(percentage);


// 3. Boolean

let isPassed = true;
let hasSubmitted = false;

console.log(isPassed);
console.log(hasSubmitted);


// 4. Undefined

let phoneNumber;

console.log(phoneNumber);


// 5. Null

let selectedCourse = null;

console.log(selectedCourse);


// 6. BigInt

let largeValue = 12345678901234567890n;

console.log(largeValue);


// 7. Symbol

let idA = Symbol("id");
let idB = Symbol("id");

console.log(idA === idB); // false


// Checking data types using typeof

console.log(typeof name);
console.log(typeof studentAge);
console.log(typeof isPassed);
console.log(typeof phoneNumber);
console.log(typeof selectedCourse);


// ===================================================
// 4. NON-PRIMITIVE DATA TYPES
// ===================================================

// 1. Array

let fruits = ["Apple", "Mango", "Banana"];

console.log(fruits);
console.log(fruits[0]);
console.log(fruits[1]);
console.log(fruits[2]);


// 2. Object

let student = {
    name: "Madhura",
    age: 20,
    course: "MCS"
};

console.log(student);
console.log(student.name);
console.log(student.age);
console.log(student.course);


// Adding properties to an object

student.city = "Pune";

console.log(student.city);


// ===================================================
// 5. STRINGS AND STRING METHODS
// ===================================================

// String declaration

let first = "Hello";
let second = "JavaScript";

console.log(first);
console.log(second);


// String concatenation

let firstName1 = "Madhura";
let lastName = "Lakade";

let fullName = firstName1 + " " + lastName;

console.log(fullName);


// Template literals

let studentName1 = "Rahul";
let studentAge1 = 20;

console.log(
    `My name is ${studentName1} and my age is ${studentAge1}.`
);


// String methods

let language = "JavaScript";

console.log(language.length);

console.log(language.toUpperCase());

console.log(language.toLowerCase());

let message = "   Hello Students   ";

console.log(message.trim());

console.log(language.includes("Script"));

console.log(language.slice(0, 4));


// ===================================================
// 6. OPERATORS
// ===================================================

// 1. Arithmetic Operators

let a = 10;
let b = 5;

console.log("Addition:", a + b);
console.log("Subtraction:", a - b);
console.log("Multiplication:", a * b);
console.log("Division:", a / b);
console.log("Modulus:", a % b);
console.log("Exponentiation:", a ** b);


// Increment and decrement

let x = 4;

x++;
console.log("Increment:", x);

x--;
console.log("Decrement:", x);


// 2. Assignment Operators

let number = 10;

number += 5;
console.log(number);

number -= 2;
console.log(number);

number *= 2;
console.log(number);

number /= 2;
console.log(number);


// 3. Comparison Operators

console.log(10 == "10");
console.log(10 === "10");

console.log(10 != 5);
console.log(10 !== "10");

console.log(10 > 5);
console.log(10 < 5);
console.log(10 >= 10);
console.log(10 <= 5);


// 4. Logical Operators

let studentAge2 = 20;
let hasID = true;

console.log(studentAge2 >= 18 && hasID === true);

let hasEmail = false;
let hasPhone = true;

console.log(hasEmail || hasPhone);

let isAbsent = false;

console.log(!isAbsent);


// 5. Ternary Operator

let ageForVoting = 20;

let eligibility = ageForVoting >= 18
    ? "Eligible"
    : "Not Eligible";

console.log(eligibility);


// ===================================================
// 7. SETS
// ===================================================

// Set stores only unique values.

let fruitSet = new Set([
    "Apple",
    "Mango",
    "Apple",
    "Banana"
]);

console.log(fruitSet);


// Creating an empty Set

let numbers = new Set();

numbers.add(10);
numbers.add(20);
numbers.add(30);
numbers.add(10);

console.log(numbers);


// Set methods

let values = new Set([10, 20, 30, 10]);

values.add(40);

console.log(values);

console.log(values.has(20));

values.delete(10);

console.log(values);

console.log("Set Size:", values.size);

// values.clear();
// console.log(values);


// ===================================================
// 8. CONTROL STRUCTURES
// ===================================================

// 1. if statement

let marks = 75;

if (marks >= 40) {
    console.log("Pass");
}


// 2. if-else statement

let marks1 = 35;

if (marks1 >= 40) {
    console.log("Pass");
} else {
    console.log("Fail");
}


// 3. if-else-if statement

let marks2 = 85;

if (marks2 >= 90) {
    console.log("Grade A+");
} else if (marks2 >= 80) {
    console.log("Grade A");
} else if (marks2 >= 60) {
    console.log("Grade B");
} else if (marks2 >= 40) {
    console.log("Grade C");
} else {
    console.log("Fail");
}


// 4. Nested if

let studentAge3 = 20;
let studentHasID = true;

if (studentAge3 >= 18) {

    if (studentHasID === true) {
        console.log("Entry Allowed");
    } else {
        console.log("ID Required");
    }

} else {
    console.log("Not Allowed");
}


// 5. Switch statement

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


// ===================================================
// 9. LOOPS
// ===================================================

// 1. FOR LOOP

for (let i = 1; i <= 5; i++) {
    console.log(i);
}


// 2. WHILE LOOP

let i = 1;

while (i <= 5) {
    console.log(i);
    i++;
}


// 3. DO-WHILE LOOP

let j = 1;

do {
    console.log(j);
    j++;
} while (j <= 5);


// 4. BREAK STATEMENT

for (let k = 1; k <= 10; k++) {

    if (k === 5) {
        break;
    }

    console.log(k);
}


// 5. CONTINUE STATEMENT

for (let m = 1; m <= 5; m++) {

    if (m === 3) {
        continue;
    }

    console.log(m);
}


// ===================================================
// 10. FUNCTIONS
// ===================================================

// 1. Function declaration

function greet() {
    console.log("Hello Students");
}

greet();


// 2. Function without parameters

function welcome() {
    console.log("Welcome to JavaScript Class");
}

welcome();


// 3. Function with parameters

function greetStudent(name) {
    console.log("Hello " + name);
}

greetStudent("Rahul");
greetStudent("Madhura");


// 4. Function with multiple parameters

function add(a, b) {
    console.log(a + b);
}

add(10, 20);
add(50, 30);


// 5. Function using return

function addition(a, b) {
    return a + b;
}

let result = addition(10, 20);

console.log("Addition:", result);


// 6. Function with condition

function checkResult(marks) {

    if (marks >= 40) {
        return "Pass";
    } else {
        return "Fail";
    }

}

console.log(checkResult(75));
console.log(checkResult(30));


// 7. Arrow Function

const multiply = (a, b) => {
    return a * b;
};

console.log("Multiplication:", multiply(4, 5));


// Arrow function with implicit return

const square = (number) => number * number;

console.log("Square:", square(5));


// ===================================================
// 11. PRACTICE QUESTION
// FUNCTION TO CALCULATE TOTAL AND AVERAGE
// ===================================================

function calculateResult(sub1, sub2, sub3) {

    let total = sub1 + sub2 + sub3;

    let average = total / 3;

    return {
        total: total,
        average: average
    };

}

let result1 = calculateResult(80, 70, 90);

console.log("Total Marks:", result1.total);
console.log("Average Marks:", result1.average);


// ===================================================
//               END OF DAY 1
// ===================================================
