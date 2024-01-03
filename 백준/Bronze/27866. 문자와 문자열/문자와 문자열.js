let input = require("fs").readFileSync("/dev/stdin").toString().trim().split("\n");

const num = +input[1] - 1;

console.log(input[0][num]);
