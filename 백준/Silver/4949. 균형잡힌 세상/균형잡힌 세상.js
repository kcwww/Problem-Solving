let input = require("fs").readFileSync("/dev/stdin").toString().trim().split("\n");

let result = "";


input.forEach((e) => {
  if (e.length === 1 && e[0] === ".") return;
  let idx = 0;
  let flag = true;
  const stack = [];
  while (e[idx] !== "." && flag) {
    if (e[idx] === "(") {
      stack.push("(");
    } else if (e[idx] === "[") {
      stack.push("[");
    } else if (e[idx] === ")") {
      const paren = stack.pop();
      if (paren === undefined || paren !== "(") flag = false;
    } else if (e[idx] === "]") {
      const paren = stack.pop();
      if (paren === undefined || paren !== "[") flag = false;
    }
    idx += 1;
  }

  if (stack.length !== 0) flag = false;
  if (flag) result += "yes\n";
  else result += "no\n";
});

result = result.slice(0, -1);


console.log(result);
