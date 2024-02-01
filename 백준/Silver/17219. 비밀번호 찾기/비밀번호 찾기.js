const file = process.platform === 'linux' ? '/dev/stdin' : 'test.txt';
const input = require('fs').readFileSync(file).toString().trim().split('\n');

const [N, M] = input.shift().split(' ').map(Number);

const arr1 = input.slice(0, N);
const arr2 = input.slice(N, N + M);

const obj = new Map();

arr1.forEach((v) => {
  const [key, value] = v.split(' ');
  obj.set(key, value);
});

let result = arr2.reduce((acc, cur) => {
  const [key, _] = cur.split(' ');
  if (obj.has(key)) {
    acc += obj.get(key) + '\n';
  }
  return acc;
}, '');

console.log(result.trim());
