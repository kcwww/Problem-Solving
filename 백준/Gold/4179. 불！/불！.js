let input = require("fs").readFileSync("/dev/stdin").toString().trim().split("\n");

const [row, col] = input[0].split(" ").map( v => +v );

const graph = input.slice(1).map((e) => [...e]);





const firstInit = (graph, col) => {
  let jihoon;
  const fire = [];

  graph.forEach((element, idx) => {
    for (let i = 0; i < col; i++) {
      if (element[i] === 'J') jihoon = [idx, i];
      else if (element[i] === 'F') fire.push([idx, i]);
    }
  });
  return [fire, jihoon];
};

const [f, j] = firstInit(graph, col);

graph[j[0]][j[1]] = "*";

const fire = [f];
const jihoon = [[j]];


const move = [[1, 0], [-1, 0], [0, 1], [0, -1]];
let result = 0;


while (fire.length) {
  const q = fire.shift();
  const next = [];
  result += 1;

  q.forEach((e) => {
    move.forEach((m) => {
      const nr = e[0] + m[0];
      const nc = e[1] + m[1];

      if (nr >= 0 && nr < row && nc >= 0 && nc < col && graph[nr][nc] === ".") {
        const str = result.toString()
        next.push([nr, nc]);
        graph[nr][nc] = str;
      }
    });
  });

  if (next.length) fire.push(next);
}


result = 0;

let escape = false;

const isSide = (arr) => {
  const [r,c] = arr;

  if (r === 0 || r === (row - 1)) return true;
  if (c === 0 || c === (col - 1)) return true;
};


while (jihoon.length) {
  const q = jihoon.shift();
  const next = [];
  result += 1;


  q.forEach((e) => {
    if (isSide(e)) escape = true;


    move.forEach((m) => {
      const nr = e[0] + m[0];
      const nc = e[1] + m[1];

      if (nr >= 0 && nr < row && nc >= 0 && nc < col) {
        if (graph[nr][nc] !== 'F' && graph[nr][nc] !== 'J' && graph[nr][nc] !== '#') {
          if (graph[nr][nc] === ".") {
            graph[nr][nc] = "*";
            next.push([nr, nc]);
          } else {
            const num = parseInt(graph[nr][nc], 10);
            if (result < num) {
              graph[nr][nc] = "*";
              next.push([nr, nc]);
            }
          }
        }
      }
    });
  });
  if (escape) break;
  if (next.length) jihoon.push(next);
}

if (escape) console.log(result);
else console.log("IMPOSSIBLE");
