const file = process.platform === 'linux' ? '/dev/stdin' : 'test.txt';
const input = require('fs').readFileSync(file).toString().trim().split('\n');

const N = +input.shift();
const arr = input.map((e) => BigInt(e));
const obj = new Map();

arr.forEach((v) => {
  if (obj.get(v) === undefined) {
    obj.set(v, 1);
  } else {
    obj.set(v, obj.get(v) + 1);
  }
});


const sorted = [...obj].sort((a, b) => {
  if (b[1] < a[1]) return -1;
  else if (b[1] > a[1]) return 1;
  else {
    if (a[0] < b[0]) return -1;
    if (a[0] > b[0]) return 1;
    else return 0;
  }
});

console.log(sorted[0][0].toString());

