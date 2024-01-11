let input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');

const [col, row] = input[0].split(' ').map(e => +e);

const graph = input.slice(1).map(e => e.split(' ').map(e => +e));

const queue = [];
const first = [];

const findInit = () => {
  graph.forEach((e, i) => {
    e.forEach((v, j) => {
      if (v === 1) first.push([i, j]);
    });
  });
}

const checkTomato = () => {
  let flag = false;
  graph.forEach(e => {
    if (e.includes(0)) flag = true;
  });
  return flag;
};


findInit();

queue.push(first);

let result = 0;

const move = [[-1, 0], [1, 0], [0, -1], [0, 1]];

while (queue.length) {
  const cur = queue.shift();
  const next = [];
  cur.forEach(e => {
    move.forEach(v => {
      const [x, y] = [e[0] + v[0], e[1] + v[1]];
      if (x >= 0 && x < row && y >= 0 && y < col && graph[x][y] === 0) {
        graph[x][y] = 1;
        next.push([x, y]);
      }
    });
  });
  if (next.length) {
    queue.push(next);
    result++;
  }
};

if (checkTomato()) result = -1;

console.log(result);
