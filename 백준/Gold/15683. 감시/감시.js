const file = process.platform === 'linux' ? '/dev/stdin' : 'test.txt';
const input = require('fs').readFileSync(file).toString().trim().split("\n");

const [Row, Col] = input[0].split(" ").map(v => +v);

const map = input.slice(1).map((e) => {return e.split(" ").map(v => +v)});




const cctv = [];
let max = 0;

map.forEach((element, row) => {
  element.forEach((e, col) => {
    if (e === 0) max += 1;
    else if (e === 6) return ;
    else cctv.push([e, row, col]);
  });
});

const cctvLen = cctv.length;


//4
const one = (r, c, map, dir) => {
  const direction = [[0,1], [1, 0], [0, -1], [-1, 0]];
  const set = '#';

  while (r >= 0 && r < Row && c >= 0 && c < Col) {
    r += direction[dir][0];
    c += direction[dir][1];
    if (!(r >= 0 && r < Row && c >= 0 && c < Col)) break;
    if (map[r][c] === 6) break;
    if (map[r][c] === 0) map[r][c] = set;
  }
};

//2
const two = (r, c, map, dir) => {
  const set = '#';
  const direction = dir === 0 ? [[0, 1], [0, -1]] : [[1, 0], [-1, 0]];

  let rR = r;
  let rC = c;
  while (r >= 0 && r < Row && c >= 0 && c < Col) {
    r += direction[0][0];
    c += direction[0][1];
    if (!(r >= 0 && r < Row && c >= 0 && c < Col)) break;
    if (map[r][c] === 6) break;
    if (map[r][c] === 0) map[r][c] = set;
  }
  r = rR;
  c = rC;
  while (r >= 0 && r < Row && c >= 0 && c < Col) {
    r += direction[1][0];
    c += direction[1][1];
    if (!(r >= 0 && r < Row && c >= 0 && c < Col)) break;
    if (map[r][c] === 6) break;
    if (map[r][c] === 0) map[r][c] = set;
  }
};

//4
const three = (r, c, map, dir) => {
  const set = '#';
  const direction = [[-1, 1], [1, 1], [1, -1], [-1, -1]];

  let tR = r;
  while (r >= 0 && r < Row && c >= 0 && c < Col) {
    r += direction[dir][0];
    if (!(r >= 0 && r < Row && c >= 0 && c < Col)) break;
    if (map[r][c] === 6) break;
    if (map[r][c] === 0) map[r][c] = set;
  }
  r = tR;
  while (r >= 0 && r < Row && c >= 0 && c < Col) {
    c += direction[dir][1];
    if (!(r >= 0 && r < Row && c >= 0 && c < Col)) break;
    if (map[r][c] === 6) break;
    if (map[r][c] === 0) map[r][c] = set;
  }
};


//4
const four = (r, c, map, dir) => {
  one(r, c, map,(dir + 2) % 4);
  three(r, c, map, dir);
};


//1
const five = (r, c, map) => {
  two(r, c, map, 0);
  two(r, c, map, 1);
};

const getNum = (map, total) => {
  const temp = map.map((element) => {return element.map(e => e)});

  total.forEach((e) => {
    const num = e[0];
    if (num === 1) one (e[1], e[2], temp, e[3]);
    else if (num === 2) two(e[1], e[2], temp, e[3]);
    else if (num === 3) three(e[1], e[2], temp, e[3]);
    else if (num === 4) four(e[1], e[2], temp, e[3]);
    else if (num === 5) five(e[1], e[2], temp);
  });

  let result = 0;
  temp.forEach((element) => {
    element.forEach((e) => {
      if (e === 0) result += 1;
    });
  })

  return result;
}

const total = [];

const backTracking = (idx) => {
  if (idx === cctvLen) {
    const diff = getNum(map, total);
    max = max >= diff ? diff : max;
    return ;
  }

  const cctvNum = cctv[idx][0];

  if (cctvNum === 1) {
    for (let i = 0; i <= 3; i++) {
      total.push([...cctv[idx], i]);
      backTracking(idx + 1);
      total.pop();
    }
  } else if (cctvNum === 2) {
    for (let i = 0; i <= 1; i++) {
      total.push([...cctv[idx], i]);
      backTracking(idx + 1);
      total.pop();
    }
  } else if (cctvNum === 3) {
    for (let i = 0; i <= 3; i++) {
      total.push([...cctv[idx], i]);
      backTracking(idx + 1);
      total.pop();
    }
  } else if (cctvNum === 4) {
    for (let i = 0; i <= 3; i++) {
      total.push([...cctv[idx], i]);
      backTracking(idx + 1);
      total.pop();
    }
  } else if (cctvNum === 5) {
    total.push([...cctv[idx]]);
    backTracking(idx + 1);
    total.pop();
  }
};

backTracking(0);

console.log(max);
