// // FS is file system Operation
// writeFileSync : is a method of node.js 
// const fs = require("fs");
// fs.writeFileSync("Student.txt", "My name is madhura");
// console.log("file created successfully");

// const fs = require("fs");
// const data = fs.readFileSync("Student.txt","utf8");
// console.log("data")

// // apend
// const fs = require("fs");
// fs.appendFileSync("Student.txt", "how are you");
// console.log("File created successfully");

// const fs = require("fs");
// const result = fs.existsSync("Student.txt");
// console.log(result)

const fs = require("fs");
fs.unlinkSync("student.txt");
console.log("File deleted successfully")