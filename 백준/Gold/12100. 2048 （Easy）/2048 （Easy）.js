const file = process.platform === 'linux' ? '/dev/stdin' : 'test.txt';
const input = require('fs').readFileSync(file).toString().trim().split("\n");

const N = +input[0];

const board = input.slice(1).map(e => e.split(" ").map(v => +v));

const dir = [[0,1], [0, -1], [1, 0], [-1, 0]];
const direction = ['L', 'R', 'U', 'D'];

let max = 0;

board.forEach((element) => {element.forEach(e => max = e >= max ? e : max)});

const Left = (board, obj) => {
  for (let j = 1; j < N; j++) {
    for (let i = 0; i < N; i++) {

      let index = j;
      while (index > 0) {
        const value = board[i][index];
        if (board[i][index - 1] === 0) {
          board[i][index - 1] = value;
          board[i][index] = 0;
        } else if (value !== 0 && value === board[i][index -1]) {
          const coordinate = i.toString() + (index - 1).toString();
          if (obj[coordinate] === undefined) {
            board[i][index - 1] = value * 2;
            max = max > (value * 2) ? max : (value * 2);
            board[i][index] = 0;
            obj[coordinate] = true;
          }
          break;
        } else break;
        index--;
      }
    }
  }
};


const Right = (board, obj) => {
  for (let j = N - 2; j >= 0; j--) {
    for (let i = 0; i < N; i++) {

      let index = j;
      while (index < N - 1) {
        const value = board[i][index];
        if (board[i][index + 1] === 0) {
          board[i][index + 1] = value;
          board[i][index] = 0;
        } else if (value !== 0 && value === board[i][index + 1]) {
          const coordinate = i.toString() + (index + 1).toString();
          if (obj[coordinate] === undefined) {
            board[i][index + 1] = value * 2;
            board[i][index] = 0;
            obj[coordinate] = true;
            max = max > (value * 2) ? max : (value * 2);
          }
          break;
        } else break;
        index++;
      }
    }
  }
};

const Up = (board, obj) => {
  for (let i = 1; i < N; i++) {
    for (let j = 0; j < N; j++) {

      let index = i;
      while (index > 0) {
        const value = board[index][j];
        if (board[index - 1][j] === 0) {
          board[index - 1][j] = value;
          board[index][j] = 0;
        } else if (value !== 0 && value === board[index - 1][j]) {
          const coordinate = (index - 1).toString() + j.toString();
          if (obj[coordinate] === undefined) {
            board[index - 1][j] = value * 2;
            board[index][j] = 0;
            obj[coordinate] = true;
            max = max > (value * 2) ? max : (value * 2);
          }
          break;
        } else break;
        index--;
      }
    }
  }

};

const Down = (board, obj) => {
  for (let i = N - 2; i >= 0; i--) {
    for (let j = 0; j < N; j++) {

      let index = i;
      while (index < N - 1) {
        const value = board[index][j];
        if (board[index + 1][j] === 0) {
          board[index + 1][j] = value;
          board[index][j] = 0;
        } else if (value !== 0 && value === board[index + 1][j]) {
          const coordinate = (index + 1).toString() + (j).toString();
          if (obj[coordinate] === undefined) {
            board[index + 1][j] = value * 2;
            board[index][j] = 0;
            obj[coordinate] = true;
            max = max > (value * 2) ? max : (value * 2);
          }
          break;
        } else break;
        index++;
      }
    }
  }
};


const move = (direction, board) => {
  const temp = board.map(element => element.map(e => e));
  const obj = {};

  switch (direction) {
    case 'L':
      Left(temp, obj);
      break;
    case 'R':
      Right(temp, obj);
      break;
    case 'U':
      Up(temp, obj);
      break;
    case 'D':
      Down(temp, obj);
      break;
  }
  return temp;
};



const backTracking = (cnt, board) => {
  if (cnt === 5) {
    return ;
  }

  direction.forEach((d) => {
    backTracking(cnt + 1, move(d, board));
  });
};

backTracking(0, board);

console.log(max);
