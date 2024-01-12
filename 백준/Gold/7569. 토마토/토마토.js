const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');
const [col, row, high] = input[0].split(' ').map(v => +v);

const graph = [];
const tomato = input.slice(1);

for (let i = 0; i < high; i++) {
  const board = [];

  const line = i * row;
  for (let j = line; j < line + row; j++) {
    const oneLine = tomato[j].split(" ").map(v => +v);
    board.push(oneLine);
  }
  graph.push(board);
}

const firstInit = (graph) => {
  const result = [];

  graph.forEach((element, zidx) => {
    element.forEach((row, yidx) => {
      row.forEach((col, xidx) => {
        if (col === 1) {
          result.push([zidx, yidx, xidx]);
        }
      });
    });
  });
  return result;
};

const queue = [];
queue.push(firstInit(graph));



let result = 0;
const move = [[1,0,0], [-1,0,0], [0,1,0], [0,-1,0], [0,0,1], [0,0,-1]];

while (queue.length) {
  const cur = queue.shift();
  const next = [];

  cur.forEach((e) => {
    const [h, r, c] = e;
    move.forEach((m) => {
      const [nh, nr, nc] = [h + m[0], r + m[1], c + m[2]];
      if (nh >= 0 && nh < high && nr >= 0 && nr < row && nc >= 0 && nc < col && graph[nh][nr][nc] === 0) {
        graph[nh][nr][nc] = 1;
        next.push([nh, nr, nc]);
      }
    });
  });
  if (next.length) {
    result += 1;
    queue.push(next);
  }
}


const checkTomato = (graph) => {
  let flag = false;
  graph.forEach((element) => {
    element.forEach(e => {
      if (e.includes(0)) flag = true;
    })
  });
  return flag;
};

if (checkTomato(graph)) result = -1;

console.log(result);
