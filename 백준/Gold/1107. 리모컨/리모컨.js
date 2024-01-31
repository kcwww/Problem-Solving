
const file = process.platform === 'linux' ? '/dev/stdin' : 'test.txt';
const [N, M, nums] = require('fs').readFileSync(file).toString().trim().split('\n');
const brokens = nums ? nums.split(' ').reduce((acc, v) => {
  acc[v] = true;
  return acc;
  }, {}) : {};

let count = Math.abs(100 - N);
for (let i = 0; i < 1000000; i++) {
    const numString = i.toString();
    let isValid = true;
    for (let j = 0; j < numString.length; j++) {
        if (brokens[numString[j]]) {
            isValid = false;
            break;
        }
    }
    if (isValid) {
        count = Math.min(count, Math.abs(i - N) + numString.length);
    }
}

console.log(count);
