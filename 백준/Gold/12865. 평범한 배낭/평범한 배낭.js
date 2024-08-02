const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const input = require("fs")
  .readFileSync(filePath)
  .toString()
  .trim()
  .split("\n");

const [num, weight] = input
  .shift()
  .split(" ")
  .map((v) => +v);

const items = input.map((v) => v.split(" ").map((v) => +v));
items.unshift([0, 0]);

const dp = Array.from({ length: weight + 1 }, () =>
  Array.from({ length: num + 1 }, () => 0)
);

for (let i = 1; i <= weight; i++) {
  for (let j = 1; j <= num; j++) {
    const [w, v] = items[j];
    if (i >= w) {
      dp[i][j] = Math.max(dp[i][j - 1], dp[i - w][j - 1] + v);
    } else {
      dp[i][j] = dp[i][j - 1];
    }
  }
}

console.log(dp[weight][num]);
