const file = process.platform === 'linux' ? '/dev/stdin' : 'test.txt';
const input = require('fs').readFileSync(file).toString().trim().split('\n');

const [N, M] = input.shift().split(' ').map(Number);


const Narr = input.slice(0, N);
const Marr = input.slice(N);

const obj = {};

Narr.forEach((v) => {
  if (!obj[v]) obj[v] = 1;
});

const result = [];

Marr.forEach((v) => {
  if (obj[v]) result.push(v);
});


result.sort();
console.log(result.length + '\n' + result.join('\n'));
