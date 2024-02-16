const file = process.platform === "linux" ? "/dev/stdin" : "test.txt";
const input = require("fs").readFileSync(file).toString().trim().split("\n");

const N = +input.shift();

const obj = {};

obj[1] = 1;
obj[2] = 2;

for (let i = 3; i <= N; i++) {
  obj[i] = (obj[i - 1] + obj[i - 2]) % 10007;
}

console.log(obj[N]);
