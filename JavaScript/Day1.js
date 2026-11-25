// console.log("Hello world");ṇ
// version check node -v, npm -v

// types of variables
// 1.let
// let age = 20;
// console.log(age);
// age = 21;
// console.log(age);

// 2.var
// it overrides the date
// var studentName = "Rahul";
// console.log(studentName);
// studentName = "Amit";
// console.log(studentName);

// 3.const
// const college = "SP";
// console.log(college);

// 

// var box1 = "sweets";
// {
//     let box2 = "chocolates";
// }

// console.log(box1);
// console.log(box2);

// a = "10";
// b = 10;
// console.log(a+b);
// console.log(a-b);
// console.log(a*b);
// console.log(a/b);
// console.log(typeof(a));
// console.log(typeof(b));

// FORMATTED STRING
// let lastname = "lakade";
// let firstname = "madhura";
// console.log(`my name is ${firstname} ${lastname}`);

// ARITHMETIC OPERATORS
// let price = 50;
// let qty = 3;
// console.log(`Total price is ${price*qty}`);

// // undefined
// let studentage;
// console.log(studentage); 

// // null
// let course = null;
// console.log(course);

// let student = 
// {
//     name : "madhura",
//     age : 20,
//     course : "MCS"
// };
// console.log(student.name);
// console.log(student.age);
// console.log(student.course);

// SYMBOL means it stores unique value
// let idA = Symbol("id");
// student[idA] = 101;

// let idB = Symbol("id");
// student[idB] = 999;

// console.log(student[idA]);
// console.log(student[idB]);
// console.log(student.name);

// let locker = {};
// locker[key1] = "iphone";

// -2 is coming undefined because it is not a valid index in the array. 
// In JavaScript, array indices are zero-based and must be non-negative integers. 
// Therefore, accessing an array with a negative index will return undefined.
// let fruits = ["apple", "mango","banana"];
// console.log(fruits);
// console.log(fruits[0]);
// console.log(fruits[1]);
// console.log(fruits[-2]);

// let name = "madhura";
// let age = 20;
// let ispassed = true;

// console.log(typeof(name));
// console.log(typeof(age));
// console.log(typeof(ispassed));

// STRING METHODS
// let named = "javascript";
// console.log(named.length);
// let named1 = "javascript";
// console.log(named1.toUpperCase());
// let named2 = "JAVASCRIPT";
// console.log(named2.toLowerCase());
// let named3 = "    madhura          ";
// console.log(named3.trim());
// let msg = "I am Learning Javascript";
// console.log(msg.includes("am"));

// slice() - extracts a portion of string
// let language = "Javascript";
// console.log(language.slice(0,4));

// the == operator checks the contents
// the === operator checks the contents and data types
// console.log(10 == "10");
// console.log(10 === "10");

// Set A 
// let fruits = new Set(["apple", "mango", "banana", "orange"]);
// console.log(fruits);

// let numbers = new Set();
// numbers.add(10);
// console.log(numbers);

// switch

//  for loop 
// for(let i = 1; i <= 10; i++)
// {
//     if(i === 5)
//     {
//         break;
//     }
//     console.log(i);
// }

//  CREATE A FUNCTION
// function function_name(paras)
// {

// }
// function greet()

// Q write func to caculate total & avg
// create a javascript func name calculateresult of 3 sub

function CalculateResult(sub1, sub2, sub3)
{
    let total = sub1 + sub2 + sub3;
    let avg = total / 3;
    console.log("total marks: ", total);
    console.log("Average marks: ", avg);
    return {
        total : total,
        average : avg
    };
}
let result = CalculateResult(98,97,99);
console.log(result);


