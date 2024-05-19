const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const input = require("fs")
  .readFileSync(filePath)
  .toString()
  .trim()
  .split("\n");

let num = +input[0];

const dp = {
  1: 0,
  2: 1,
  3: 1,
};

const pre = {
  1: 0,
  2: 1,
  3: 1,
};

for (let i = 4; i <= num; i++) {
  dp[i] = dp[i - 1] + 1;
  pre[i] = i - 1;
  if (i % 2 === 0 && i % 3 === 0) {
    dp[i] = Math.min(dp[i / 2] + 1, dp[i / 3] + 1, dp[i]);
    if (dp[i] === dp[i / 2] + 1) pre[i] = i / 2;
    else if (dp[i] === dp[i / 3] + 1) pre[i] = i / 3;
  } else if (i % 2 === 0) {
    dp[i] = Math.min(dp[i / 2] + 1, dp[i]);
    if (dp[i] === dp[i / 2] + 1) pre[i] = i / 2;
  } else if (i % 3 === 0) {
    dp[i] = Math.min(dp[i / 3] + 1, dp[i]);
    if (dp[i] === dp[i / 3] + 1) pre[i] = i / 3;
  }
}

let result = String(dp[num]) + "\n" + String(num) + " ";

while (num !== 1) {
  num = pre[num];
  result += String(num) + " ";
}

console.log(result.trim());
