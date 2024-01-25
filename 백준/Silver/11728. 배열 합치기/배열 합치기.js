const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split("\n");

const [N, M] = input[0].split(" ").map(v => +v);

const A = input[1].split(" ").map(v => +v);
const B = input[2].split(" ").map(v => +v);

let adx = 0;
let bdx = 0;
const result = [];

while (adx < N || bdx < M) {
  if (adx === N) result.push(B[bdx++]);
  else if (bdx === M) result.push(A[adx++]);
  else if (A[adx] < B[bdx]) result.push(A[adx++]);
  else result.push(B[bdx++]);
}

console.log(result.join(' '));
