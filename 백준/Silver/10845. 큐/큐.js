let input = require("fs").readFileSync("/dev/stdin").toString().trim().split("\n");

const operation = input.slice(1).map((e)=>{return e.split(" ")});

const queue = [];

let result = "";

operation.forEach((e)=>{
  const oper = e[0];
  if (oper === "push") {
    const num = parseInt(e[1], 10);
    queue.push(num);
  } else if (oper === "size") {
    result += (queue.length + "\n");
  } else if (oper === "empty") {
    result += ((queue.length === 0 ? 1 : 0) + "\n");
  } else if (oper === "pop") {
    let num = queue.shift();
    if (num === undefined) num = -1;
    result += (num + "\n");
  } else if (oper === "front") {
    let num = queue[0];
    if (num === undefined) num = -1;
    result += (num + "\n");
  } else if (oper === "back") {
    let num = queue.at(-1);
    if (num === undefined) num = -1;
    result += (num + "\n");
  }
})

console.log(result);
