const file = process.platform === 'linux' ? '/dev/stdin' : 'test.txt';
let input = require('fs').readFileSync(file).toString().trim().split("\n");

const [row, col, block] = input[0].split(" ").map(v => +v);

const ground = input.slice(1).map((e) => {
  return e.split(" ").map(v => +v);
})

const maxFloor = 256;
const obj = {}

const one = (diff, tmp) => {
  return [diff * 2, tmp + diff]
}

const two = (diff, tmp) => {
  return [diff, tmp - diff];
}

for (let b = 0; b <= maxFloor; b++) {
  let temp = block
  let time = 0;
  let i = 0;

  while (i < row) {
    let j = 0;
    while (j < col) {
      if (ground[i][j] >= b) {
        const diff = ground[i][j] - b;
        const [add, result] = one(diff, temp);
        time += add;
        temp = result;
      } else {
        const diff = b - ground[i][j];
        const [add, result] = two(diff, temp);
        time += add;
        temp = result;
      }
      j++;
    }
    i++;
  }
  if (temp < 0) continue;
  obj[b] = time;
}

const sortedEntries = Object.entries(obj).sort((a, b) => {
  if (a[1] === b[1]) return b[0] - a[0];
  return a[1] - b[1]
});


const result = sortedEntries[0][1] + " " + sortedEntries[0][0];

console.log(result);
