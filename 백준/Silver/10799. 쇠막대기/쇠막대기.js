let input = require("fs").readFileSync("/dev/stdin").toString().trim().split("\n");

const data = input[0];
const stack = [];

let result = 0;
let temp = 0;

Array.prototype.forEach.call(data, char => {
  if (char === "(") {
    temp += 1;
    result += 1;
  } else if (char === ")") {
    const last = stack.at(-1);
    if (last === "(") {
      temp -= 1;
      result -= 1;
      result += temp;
    } else {
      temp -= 1;
    }
  }
  stack.push(char);
});

console.log(result);
