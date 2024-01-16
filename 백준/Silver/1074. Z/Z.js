const file = process.platform === 'linux' ? '/dev/stdin' : 'test.txt';
let input = require('fs').readFileSync(file).toString().trim().split('\n');

const [N, r, c] = input[0].split(' ').map(v => +v);

const recursive = (N, r, c) => {
  if (N === 0) return 0;
  const half = 1 << (N - 1);
  if (r < half && c < half) return recursive(N - 1, r, c);
  else if (r < half && c >= half) return (half * half) + recursive(N - 1, r, c - half);
  else if (r >= half && c < half) return (2 * half * half) + recursive(N - 1, r - half, c);
  else if (r >= half && c >= half) return (3 * half * half) + recursive(N - 1, r - half, c - half);
};

console.log(recursive(N, r, c));
