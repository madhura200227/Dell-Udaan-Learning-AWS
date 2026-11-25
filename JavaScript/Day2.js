// // FS is file system Operation
// writeFileSync : is a method of node.js 
// const fs = require("fs");
// fs.writeFileSync("Student.txt", "My name is madhura");
// console.log("file created successfully");

// const fs = require("fs");
// const data = fs.readFileSync("Student.txt","utf8");
// console.log("data");

// // apend
// const fs = require("fs");
// fs.appendFileSync("Student.txt", "how are you");
// console.log("File created successfully");

// const fs = require("fs");
// const result = fs.existsSync("Student.txt");
// console.log(result);

// const fs = require("fs");
// fs.unlinkSync("student.txt");
// console.log("File deleted successfully");

// types of errors in JS

// // SYNTAX ERROR
// console.log("Hello World 
// // REFERENCE ERROR ReferenceError: studentName is not defined
// console.log(studentName);
// // TYPE ERROR
// const age = 11;
// age.toUpperCase();
// // RANGE ERROR
// const badlist = [-2]

// // EXCEPTION HANDLING
// try
// {
//     // code that produces error
// }
// catch
// {
//     // handle the error
// }
// try
// {
//     console.log(studentName);
// }
// catch (error)
// {
//     console.log("something went wrong")
// }

// error.message provides descriptive message
// error.name gives error's type or name of the error
// try
// {
//     console.log(studentName);
// }
// catch (error)
// {
//     console.log(error.message);
// }

// try 
// {
//     const age =25;
//     age.toUpperCase();
// }
// catch (error)
// {
//     console.log("error name", error.name);
//     console.log("error message", error.message)
// }

// try
// {
//     console.log("Program Started");
//     console.log(studentName);
// }
// catch (error)
// {
//     console.log("Error Occured");
// }
// finally
// {
//     console.log("Exiting the program")
// }

// try
// {
//     let named = ("my name is madhura");
//     console.log(named);
//     console.log(named.toUpperCase());    
// }
// catch (error)
// {
//     console.log("Error Name : ", error.name);
//     console.log("Error Message : ", error.message)
// }
// finally
// {
//     console.log("Program executed")
// }

// const mark = 25;
// try
// {
//     if (marks < 40)
//     {
//         throw new Error("Student Has Failed");
//     }
//     console.log("Student has passed");
// }
// catch (error)
// {
//     console.log("error name: ", error.name);
//     console.log("error message: ", error.message);
// }

// MULTIPLE ERROR
// try{
//     const age = 22;
//     age.toUpperCase();
// }
// catch (error)
// {
//     if (error.name === "TypeError")
//     {
//         console.log("Wrong data type");
//     }
//     else if(error.name === "ReferencError")
//     {
//         console.log("variable not found");
//     }
//     else
//     {
//         console.log("some other error occured");
//     }
// }

// Q1
const fs = require("fs");

// Create a file
fs.writeFileSync(
    "Student.txt",
    "Student name : Madhura, Course : JS, Duration : 3 months"
);

console.log("File created successfully");

// Read the file
const data = fs.readFileSync("Student.txt", "utf8");
console.log("Before modification:");
console.log(data);

// Append content to the file
fs.appendFileSync("Student.txt", "\nHii How are you??????");

console.log("Modified the file");

// Read again to see the updated content
const updatedData = fs.readFileSync("Student.txt", "utf8");

console.log("After modification:");
console.log(updatedData);

// js prog to create and manage a student record using file handling, exception handling