const file = process.platform === 'linux' ? '/dev/stdin' : 'test.txt';
let input = require('fs').readFileSync(file).toString().trim().split('\n');

let num = parseInt(input[0], 10);

let numbers = input.slice(1).map(v => +v).sort((a,b) => a - b);
const length = numbers.length;

let average = 0;
const senterNum = numbers[Math.floor(length / 2)];
const obj = {};
const range = numbers.at(-1) - numbers[0];

numbers.forEach((v) => {
  if (obj[v] === undefined) obj[v] = 1;
  else obj[v] += 1;

  average += v;
});

average = Math.round(average / length);

let objArr = Object.entries(obj).sort((a,b) => {
  if (b[1] === a[1]) return a[0] - b[0];
  return b[1] - a[1];
});
const modeNum = objArr[0][1];
objArr = objArr.filter((e) => {
  if (modeNum === e[1]) return e;
});



let mode;
if (objArr.length >= 2) mode = objArr[1][0];
else mode = objArr[0][0];


const result = average + '\n' + senterNum + '\n' + mode + '\n' + range;

console.log(result);
