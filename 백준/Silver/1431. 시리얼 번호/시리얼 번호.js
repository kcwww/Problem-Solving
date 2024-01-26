const file = process.platform === 'linux' ? '/dev/stdin' : 'test.txt';
const input = require('fs').readFileSync(file).toString().trim().split('\n');

const N = +input.shift();
const arr = input;

arr.sort((a, b) => {
  if (a.length !== b.length) {
    return a.length - b.length;
  }

  let aSum = 0;
  let bSum = 0;
  for (let i = 0; i < a.length; i++) {
    if (!isNaN(a[i])) {
      aSum += +a[i];
    }
    if (!isNaN(b[i])) {
      bSum += +b[i];
    }
  }
  if (aSum !== bSum) {
    return aSum - bSum;
  }

  return a.localeCompare(b);
});

console.log(arr.join('\n'));
