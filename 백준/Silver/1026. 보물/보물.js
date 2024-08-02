const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const input = require("fs")
  .readFileSync(filePath)
  .toString()
  .trim()
  .split("\n");

const num = +input.shift();

const A = input
  .shift()
  .split(" ")
  .map((v) => +v);

const B = input
  .shift()
  .split(" ")
  .map((v) => +v);

A.sort((a, b) => a - b);
B.sort((a, b) => b - a);

let sum = 0;

for (let i = 0; i < num; i++) {
  sum += A[i] * B[i];
}

console.log(sum);
