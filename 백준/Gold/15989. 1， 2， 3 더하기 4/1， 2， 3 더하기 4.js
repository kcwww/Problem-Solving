const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const input = require("fs")
  .readFileSync(filePath)
  .toString()
  .trim()
  .split("\n");

let tc = Number(input.shift());

let dp = Array.from(Array(10001), () => Array(4).fill(0));

dp[1][1] = 1;
dp[2][1] = 1;
dp[2][2] = 1;
dp[3][1] = 1;
dp[3][2] = 1;
dp[3][3] = 1;

for (let i = 4; i <= 10000; i++) {
  dp[i][1] = dp[i - 1][1];
  dp[i][2] = dp[i - 2][1] + dp[i - 2][2];
  dp[i][3] = dp[i - 3][1] + dp[i - 3][2] + dp[i - 3][3];
}

for (let t = 0; t < tc; t++) {
  let n = Number(input.shift());

  console.log(dp[n][1] + dp[n][2] + dp[n][3]);
}
