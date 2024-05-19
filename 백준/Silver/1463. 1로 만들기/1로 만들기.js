const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const input = require("fs")
  .readFileSync(filePath)
  .toString()
  .trim()
  .split("\n");

const num = +input[0];

const dp = {
  1: 0,
  2: 1,
  3: 1,
};

for (let i = 4; i <= num; i++) {
  dp[i] = dp[i - 1] + 1;
  if (i % 2 === 0 && i % 3 === 0)
    dp[i] = Math.min(dp[i / 2] + 1, dp[i / 3] + 1, dp[i]);
  else if (i % 2 === 0) dp[i] = Math.min(dp[i / 2] + 1, dp[i]);
  else if (i % 3 === 0) dp[i] = Math.min(dp[i / 3] + 1, dp[i]);
}

console.log(dp[num]);
