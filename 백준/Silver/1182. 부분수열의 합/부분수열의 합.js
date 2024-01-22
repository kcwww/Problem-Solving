const file = process.platform === 'linux' ? '/dev/stdin' : 'test.txt';
const input = require('fs').readFileSync(file).toString().trim().split("\n");

const [N, S] = input[0].split(" ").map(v => +v);

const numbers = input[1].split(" ").map(v => +v);

let result = 0;

const backTracking = (idx, total) => {

  if (idx === N - 1) {
    if (total === S) {
      result += 1
    };
    return ;
  };
  idx += 1;
  backTracking(idx, total + numbers[idx]);
  backTracking(idx, total);
};

backTracking(-1, 0);

if (S === 0) result -= 1;

console.log(result);
