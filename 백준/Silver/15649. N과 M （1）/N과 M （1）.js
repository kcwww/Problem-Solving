const file = process.platform === 'linux' ? '/dev/stdin' : 'test.txt';
const input = require('fs').readFileSync(file).toString().trim().split("\n");

const [N, M] = input[0].split(" ").map(v => +v);

const range = new Array(N).fill(1).map((n , i) => n + i);

const current = [];

let result = '';

const backTracking = (idx) => {

  if (idx === M) {
    current.forEach((e) => {
      result += (e + ' ');
    });
    result.trim();
    console.log(result);
    result ='';
    return;
  }

  for (let i = 0; i < N; i++) {
    if (current.includes(range[i])) continue;
    current.push(range[i]);
    backTracking(idx + 1);
    current.pop();
  }
};

backTracking(0);


