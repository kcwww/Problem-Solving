let input = require("fs").readFileSync("/dev/stdin").toString().trim().split("\n");

const numArray = input[1].split(" ").map(v => +v);
const checkArray = input[3].split(" ").map(v => +v);

const obj = {};

numArray.forEach(v => {
    if (obj[v]) obj[v]++;
    else obj[v] = 1;
});

let str = "";

checkArray.forEach((e) => {
  const numStr = e.toString();
  const num = obj[numStr];
  if (num !== undefined) str += (num);
  else str += "0";
  str += " ";
});

console.log(str);
