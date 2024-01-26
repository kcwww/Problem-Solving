const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split("\n");

const [N, M] = input[0].split(" ").map(v => +v);

const A = input[1].split(" ").map(v => +v);
const B = input[2].split(" ").map(v => +v);

let adx = 0;
let bdx = 0;
const result = new Array(N + M).fill(0);
let idx = 0;

while (adx < N || bdx < M) {
  if (adx === N) result[idx] = (B[bdx++]);
  else if (bdx === M) result[idx] = (A[adx++]);
  else if (A[adx] < B[bdx]) result[idx] = (A[adx++]);
  else result[idx] = (B[bdx++]);
  idx++;
}

console.log(result.join(' '));
