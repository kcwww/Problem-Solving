const file = process.platform === "linux" ? "/dev/stdin" : "test.txt";
const input = require("fs").readFileSync(file).toString().trim().split("\n");

const N = +input[0];

let result = 0;


const obj = {
  1: 0,
  2: 1,
  3: 1,
};

const dp = (n) => {
  if (obj[n] !== undefined) {
    return obj[n];
  }

  if (n % 3 === 0 && n % 2 === 0) {
    obj[n] = Math.min(dp(n / 3), dp(n / 2), dp(n - 1)) + 1;
  } else if (n % 3 === 0) {
    obj[n] = Math.min(dp(n / 3), dp(n - 1)) + 1;
  } else if (n % 2 === 0) {
    obj[n] = Math.min(dp(n / 2), dp(n - 1)) + 1;
  } else {
    obj[n] = dp(n - 1) + 1;
  }
  return obj[n];
};

console.log(dp(N));
