const file = process.platform === "linux" ? "/dev/stdin" : "test.txt";
const input = require("fs").readFileSync(file).toString().trim().split("\n");

let N = +input.shift();

let result = "";

while (N > 0) {
  const arrLength = +input.shift();
  const arr = input.splice(0, arrLength).map((el) => el.split(" "));
  const obj = {};

  arr.forEach((el) => {
    if (obj[el[1]] === undefined) {
      obj[el[1]] = 2;
    } else {
      obj[el[1]] += 1;
    }
  });
  let answer = 1;
  for (let key in obj) {
    answer *= obj[key];
  }
  result += answer - 1 + "\n";
  N--;
}

console.log(result.trim());
