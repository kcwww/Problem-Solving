const file = process.platform === 'linux' ? '/dev/stdin' : 'test.txt';
let input = require('fs').readFileSync(file).toString().trim().split('\n');

const num = +input[0];

let result = Math.pow(2, num) - 1;
let content = '';

const move = (s, to) => {
  const str = s.toString() + ' ' + to.toString() + '\n';
  content += str;
};

const hanoi = (s, to, via, number) => {
  if (number === 1) {
    move(s, to);
    return ;
  } else {
    hanoi(s, via, to, number - 1);
    move(s, to);
    hanoi(via, to, s, number - 1);
  }
};

hanoi(1, 3, 2, num);

result = result.toString() + '\n' + content.trim();
console.log(result);
