## 옹뇽뇽

### 자바스크립트로 진행하는 코딩테스트 준비

```javascript

const file = process.platform === 'linux' ? '/dev/stdin' : 'test.txt';
let input = require("fs").readFileSync(file).toString().trim().split("\n")


/**
 * 입력을 받는 파트
 * split을 하게 되면 값타입이 string되기에 number로 만들어 줘야 한다.
 */
const [N, M] = input[0].split(" ").map(v => +v)
const arr = input.slice(1).map(v => v.split(" ").map(v => +v))

/*
    로직
*/

/**
 * console.log은 무겁다. 최대한 string에 담아서 한번에 출력하도록 하자.
 */
const print = ans.map((row) => row.join(" ")).join("\n")
console.log(print)



// 순열
function permutation(arr, selectNum) {
    let result = [];
    if (selectNum === 1) return arr.map((v) => [v]);

    arr.forEach((v, idx, arr) => {
        const fixer = v;
        const restArr = arr.filter((_, index) => index !== idx);
        const permuationArr = permutation(restArr, selectNum - 1);
        const combineFixer = permuationArr.map((v) => [fixer, ...v]);
        result.push(...combineFixer);
    });
    return result;
}

//  조합
function combination(arr, selectNum) {
    const result = [];
    if (selectNum === 1) return arr.map((v) => [v]);
    arr.forEach((v, idx, arr) => {
        const fixed = v;
        const restArr = arr.slice(idx + 1);
        const combinationArr = combination(restArr, selectNum - 1);
        const combineFix = combinationArr.map((v) => [fixed, ...v]);
        result.push(...combineFix);
    });
    return result;
}

//  중복순열
function permutation(arr, selectNum) {
    const result = [];
    if (selectNum === 1) return arr.map((v) => [v]);

    arr.forEach((v, idx, arr) => {
        const fixed = v;
        const restArr = arr;
        const permutationArr = permutation(restArr, selectNum - 1);
        const combineFix = permutationArr.map((v) => [fixed, ...v]);
        result.push(...combineFix);
    });
    return result;
}

// 큐

class Queue {
  constructor() {
    this.storage = {};
    this.front = 0;
    this.rear = 0;
  }
  
  size() {
    if (this.storage[this.rear] === undefined) {
      return 0;
    } else {
      return this.rear - this.rear + 1;
    }
  }
  
  add(value) {
    if (this.size() === 0) {
      this.storage['0'] = value;
    } else {
      this.rear += 1;
      this.storage[this.rear] = value;
    }
  }
  
  popleft() {
    let temp;
    if (this.front === this.rear) {
      temp = this.storage[this.front];
      delete this.storage[this.front];
      this.front = 0;
      this.rear = 0;
    } else {
      temp = this.storage[this.front];
      delete this.storage[this.front];
      this.front += 1;
    }
    return temp;
  }
}
```
