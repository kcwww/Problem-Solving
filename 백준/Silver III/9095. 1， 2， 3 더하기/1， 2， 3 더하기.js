const file = process.platform === "linux" ? "/dev/stdin" : "test.txt";
const input = require("fs").readFileSync(file).toString().trim().split("\n");

const N = +input.shift();

const number = input.map((el) => +el);

const max = Math.max(...number) + 1;
const dp = Array(max).fill(0);

dp[1] = 1;
dp[2] = 2;
dp[3] = 4;

for (let i = 4; i < max; i++) {
  dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3];
}

let result = "";

number.forEach((el) => {
  result += `${dp[el]}\n`;
});

console.log(result.trim());
