const file = process.platform === "linux" ? "/dev/stdin" : "test.txt";
let input = require("fs")
  .readFileSync(file)
  .toString()
  .trim()
  .split("\n")
  .map((v) => +v);

const N = input.shift();

const sorted = input.slice().sort((a, b) => b - a);

let max = 0;
for (let i = 0; i < sorted.length; i++) {
  max = Math.max(max, sorted[i] * (i + 1));
  
}

console.log(max);
