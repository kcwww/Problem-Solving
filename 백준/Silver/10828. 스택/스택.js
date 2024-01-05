let input = require("fs").readFileSync("/dev/stdin").toString().trim().split("\n");

const operation = input.slice(1).map((e)=>{return e.split(" ")});

const stack = [];

let result = "";

operation.forEach((e)=>{
  const oper = e[0];
  if (oper === "push") {
    const num = parseInt(e[1], 10);
    stack.push(num);
  } else if (oper === "top") {
    let num = stack.at(-1);
    if (num === undefined) num = -1;
    result += (num + "\n");
  } else if (oper === "size") {
    result += (stack.length + "\n");
  } else if (oper === "empty") {
    result += ((stack.length === 0 ? 1 : 0) + "\n");
  } else if (oper === "pop") {
    let num = stack.pop();
    if (num === undefined) num = -1;
    result += (num + "\n");
  }
})

console.log(result);
