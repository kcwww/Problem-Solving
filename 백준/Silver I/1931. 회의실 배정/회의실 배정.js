const file = process.platform === "linux" ? "/dev/stdin" : "test.txt";
const input = require("fs").readFileSync(file).toString().trim().split("\n");

const N = +input.shift();

const arr = input.map((e) => e.split(" ").map((i) => +i));

arr.sort((a, b) => {
  if (a[1] === b[1]) return a[0] - b[0];
  return a[1] - b[1];
});

let result = 1;

current = arr[0];

for (let i = 1; i < N; i++) {
  if (current[1] <= arr[i][0]) {
    result++;
    current = arr[i];
  }
}

console.log(result);
