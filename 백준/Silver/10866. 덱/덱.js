let input = require("fs").readFileSync("/dev/stdin").toString().trim().split("\n");

const operation = input.slice(1).map((e)=>{return e.split(" ")});

const deque = [];

let result = "";

operation.forEach((e)=>{
  const oper = e[0];
  if (oper === "push_back") {
    const num = parseInt(e[1], 10);
    deque.push(num);
  } else if (oper === "push_front") {
    const num = parseInt(e[1], 10);
    deque.unshift(num);
  } else if (oper === "size") {
    result += (deque.length + "\n");
  } else if (oper === "empty") {
    result += ((deque.length === 0 ? 1 : 0) + "\n");
  } else if (oper === "pop_front") {
    let num = deque.shift();
    if (num === undefined) num = -1;
    result += (num + "\n");
  } else if (oper === "pop_back") {
    let num = deque.pop();
    if (num === undefined) num = -1;
    result += (num + "\n");
  } else if (oper === "front") {
    let num = deque[0];
    if (num === undefined) num = -1;
    result += (num + "\n");
  } else if (oper === "back") {
    let num = deque.at(-1);
    if (num === undefined) num = -1;
    result += (num + "\n");
  }
})

console.log(result);
