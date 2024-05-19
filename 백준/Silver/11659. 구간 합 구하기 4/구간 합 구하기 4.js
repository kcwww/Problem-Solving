const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const input = require("fs")
  .readFileSync(filePath)
  .toString()
  .trim()
  .split("\n");

const [N, M] = input
  .shift()
  .split(" ")
  .map((v) => +v);

const arr = input
  .shift()
  .split(" ")
  .map((v) => +v);

const dp = new Array(N).fill(0);

dp[0] = arr[0];

for (let i = 1; i < N; i++) {
  dp[i] = dp[i - 1] + arr[i];
}

let result = "";

input.forEach((e) => {
  const [a, b] = e.split(" ").map((v) => +v);

  if (a === 1) result += dp[b - 1];
  else result += dp[b - 1] - dp[a - 2];

  result += "\n";
});

console.log(result.trim());
