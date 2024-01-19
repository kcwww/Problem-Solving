const file = process.platform === 'linux' ? '/dev/stdin' : 'test.txt';
let input = require('fs').readFileSync(file).toString().trim().split('\n');

let num = parseInt(input[0], 10);

let numbers = input.slice(1).map(v => +v);

const subPerson = Math.round(num * 0.15);


numbers.sort((a, b) => a - b);

if (subPerson === 0) numbers = numbers.slice(0);
else numbers = numbers.slice(subPerson, -subPerson);

const result = Math.round(numbers.reduce((acc, cur) => acc + cur, 0) / numbers.length);

if (num === 0) console.log(0);
else console.log(result);
