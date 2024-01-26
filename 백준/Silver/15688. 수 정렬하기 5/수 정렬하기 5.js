const file = process.platform === 'linux' ? '/dev/stdin' : 'test.txt';
const input = require('fs').readFileSync(file).toString().trim().split('\n');

const N = +input.shift();
const arr = input.map(Number);

const tmp = new Array(2000001).fill(0);

arr.forEach((e) => {
  tmp[e + 1000000] += 1;
});

let result = '';
tmp.forEach((e, idx) => {
  if (e > 0) {
    let cnt = e;
    while (cnt) {
      result += (idx - 1000000 + '\n')
      cnt--;
    }
  };
});

console.log(result.trim());

