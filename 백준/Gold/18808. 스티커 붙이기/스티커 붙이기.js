const file = process.platform === 'linux' ? '/dev/stdin' : 'test.txt';
const input = require('fs').readFileSync(file).toString().trim().split("\n");

const [row, col, stickerNum] = input[0].split(" ").map(v => +v);
let stickerDetail = input.slice(1);
const stickers = [];
for (let i = 0; i < stickerNum; i++) {
  const [sr, sc] = stickerDetail[0].split(" ").map(v => +v);
  const sticker = stickerDetail.slice(1, 1 + sr).map((element) => {return element.split(" ").map(v => +v);});
  stickers.push(sticker);
  stickerDetail = stickerDetail.slice(1 + sr);
}

const notebook = [];
for (let i = 0; i < row; i++) {
  const line = new Array(col).fill(0);
  notebook.push(line);
}





const rotate = (sticker) => {
  const r = sticker.length;
  const c = sticker[0].length;

  const newArr = [];
  for (let i = 0; i < c; i++) {
    const arr = new Array(r).fill(0);
    newArr.push(arr);
  }

  for (let i = 0; i < r; i++) {
    for (let j = 0; j < c; j++) {
      newArr[j][r - 1 - i] = sticker[i][j];
    }
  }
  return newArr;
};

const checkPaste = (notebook, x, y, sticker) => {
  const r = sticker.length;
  const c = sticker[0].length;



  for (let i = 0; i < r; i++) {
    for (let j = 0; j < c; j++) {
      const tx = x + i;
      const ty = y + j;

      if (sticker[i][j] === 1 && !(tx >= 0 && tx < row && ty >= 0 && ty < col)) {
        return false;
      }
      if (sticker[i][j] === 1 && notebook[tx][ty] === 1) return false;

    }
  }

  for (let i = 0; i < r; i++) {
    for (let j = 0; j < c; j++) {
      if (sticker[i][j] === 1) notebook[x+i][y+j] = 1;
    }
  }
  return true;
};

let idx = 0;
let ridx = 0;

while (idx < stickerNum) {
  let sticker = stickers[idx];
  if (ridx === 4) {
    idx += 1;
    ridx = 0;
    continue;
  }
  for (let i = 0; i < ridx; i++) {
    sticker = rotate(sticker);
  }

  let flag = false;

  for (let i = 0; i < row; i++) {
    for (let j = 0; j < col; j++) {
      if (checkPaste(notebook, i, j, sticker)) {
        flag = true;
        idx += 1;
        break;
      }
    }
    if (flag) break;
  }

  if (flag) ridx = 0;
  else ridx += 1;
}

let result = 0;

notebook.forEach((element) => {
  element.forEach((e) => {
    if (e === 1) result += 1;
  })
})

console.log(result);
