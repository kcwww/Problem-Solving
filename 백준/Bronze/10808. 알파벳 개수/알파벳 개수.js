let input = require("fs").readFileSync("/dev/stdin").toString().trim().split("\n");

const word = input[0];

const alphaAscii = 97;

const result = new Array(26).fill(0);

for (let i = 0; i < word.length; i++) {
  const num = word.charCodeAt(i) - alphaAscii;
  result[num] += 1;
}

console.log(result.join(" "));
