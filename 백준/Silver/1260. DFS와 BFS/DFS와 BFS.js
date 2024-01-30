const file = process.platform === 'linux' ? '/dev/stdin' : 'test.txt';
const input = require('fs').readFileSync(file).toString().trim().split('\n');

const [N, M, V] = input.shift().split(" ").map(Number);

const number = {};

input.forEach((e) => {
  const [a, b] = e.split(" ").map(Number);
  if (number[a] === undefined) number[a] = [];
  number[a].push(b);

  if (number[b] === undefined) number[b] = [];
  number[b].push(a);
});

for (let i = 1; i <= N; i++) {
  if (number[i]) number[i].sort((a, b) => a - b);
}



const bfs = () => {
  if (number[V] === undefined) return null;
  const visited = {};
  visited[V] = true;
  const result = [V];

  const queue = [...number[V]];
  while (queue.length !== 0) {
    const num = queue.shift();
    if (visited[num]) continue;
    visited[num] = true;
    result.push(num);

    number[num].forEach((e) => {
      if (visited[e]) return;
      queue.push(e);
    });
  }
  return result;
};

const result = [];
const visited = {};


const dfs = (start) => {
  if (visited[start]) return;
  else visited[start] = true;
  result.push(start);

  const arr = number[start];
  arr.forEach(e => dfs(e));
};

if (number[V] !== undefined) {
  dfs(V);
  console.log(result.join(" ") + "\n" + bfs().join(" "));
} else {
  console.log(V + "\n" + V);
}
