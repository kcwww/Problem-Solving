const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const input = require("fs")
  .readFileSync(filePath)
  .toString()
  .trim()
  .split("\n");

const N = +input.shift();

// dp[i][j]
const dp = Array.from(new Array(N), () => new Array(3).fill(0));

dp[0] = input.shift().split(" ").map(Number);

for (let i = 1; i < N; i++) {
  const [r, g, b] = input[i - 1].split(" ").map(Number);

  dp[i][0] = Math.min(dp[i - 1][1], dp[i - 1][2]) + r;
  dp[i][1] = Math.min(dp[i - 1][0], dp[i - 1][2]) + g;
  dp[i][2] = Math.min(dp[i - 1][0], dp[i - 1][1]) + b;
}

console.log(dp[N - 1].sort((a, b) => a - b)[0]);
