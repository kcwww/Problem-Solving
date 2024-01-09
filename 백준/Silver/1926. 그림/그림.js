let input = require("fs").readFileSync("/dev/stdin").toString().trim().split("\n");

const [row, col] = input[0].split(" ").map((v) => +v);

input = input.slice(1);

const graph = input.map((v) => v.split(" ").map((v) => +v));

let max = 0;
let picture = 0;

const bfs = (graph, row, col, i, j) => {
  let cnt = 0;
  const queue = [[i, j]];
  const move = [[1,0], [-1,0], [0, 1], [0, -1]];

  while (queue.length) {
    const [x,y] = queue.pop();
    if (graph[x][y] === 0) continue;
    graph[x][y] = 0;
    cnt += 1;

    for (let m = 0; m < 4; m++) {
      let nx = x + move[m][0];
      let ny = y + move[m][1];

      if (nx >= 0 && nx < row && ny >= 0 && ny < col) {
        if (graph[nx][ny] === 1) queue.push([nx, ny]);
      }
    }
  }
  return cnt;
};

for (let i = 0; i < row; i++) {
  for (let j = 0; j < col; j++) {
    if (graph[i][j] === 1) {
      picture += 1;
      let cnt = bfs(graph, row, col, i, j);
      max = (max >= cnt ? max : cnt);
    }
  }
}

const result = picture.toString() + "\n" + max;

console.log(result);

