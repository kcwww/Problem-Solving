const file = process.platform === 'linux' ? '/dev/stdin' : 'test.txt';
let input = require('fs').readFileSync(file).toString().trim().split('\n');

let num = BigInt(parseInt(input[0], 10));

let result = 0;
let value = BigInt(1);

while (num > 0) {
  value *= num;
  if (value >= 10n && value % 10n == 0) {
    value /= 10n;
    result += 1;
  }
  num--;
}

console.log(result);
