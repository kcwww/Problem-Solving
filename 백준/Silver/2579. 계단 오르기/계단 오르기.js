const file = process.platform === "linux" ? "/dev/stdin" : "test.txt";
const input = require("fs").readFileSync(file).toString().trim().split("\n");

const N = +input.shift();

const number = input.map((el) => +el);

const obj = {};

for (let i = 1; i <= N; i++) {
  obj[i] = [0, 0];
}

obj[1] = [number[0], 0];
obj[2] = [number[0] + number[1], number[1]];

const dp = (step) => {
  for (let i = 3; i <= step; i++) {
    obj[i][0] = obj[i - 1][1] + number[i - 1];
    obj[i][1] = Math.max(obj[i - 2][0], obj[i - 2][1]) + number[i - 1];
  }
};

dp(N);

console.log(Math.max(...obj[N]));
