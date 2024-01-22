const file = process.platform === 'linux' ? '/dev/stdin' : 'test.txt';
const input = require('fs').readFileSync(file).toString().trim().split("\n");

const N = +input[0];

const board = new Array(N).fill(0);

let result = 0;

const promising = (row) => {
  for (let i = 0; i < row; i++) {
    if (board[row] == board[i] || row - i == Math.abs(board[row] - board[i])) return false;
  }
  return true;
};


const N_Queens = (row) => {
  if (row === N) {
    result += 1;
    return ;
  }

  for (let i = 0; i < N; i++) {
    board[row] = i;
    if (promising(row)) {
      N_Queens(row + 1);
    }
  }
};

N_Queens(0);

console.log(result);
