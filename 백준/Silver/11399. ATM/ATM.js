const file = process.platform === "linux" ? "/dev/stdin" : "test.txt";
const input = require("fs").readFileSync(file).toString().trim().split("\n");

const N = +input[0];

const personArr = input[1]
  .split(" ")
  .map(Number)
  .sort((a, b) => a - b);

let sum = 0;
let result = 0;

personArr.forEach((person) => {
  sum += person;
  result += sum;
});

console.log(result);
