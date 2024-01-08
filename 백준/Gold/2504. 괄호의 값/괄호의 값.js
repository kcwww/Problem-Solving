let input = require("fs").readFileSync("/dev/stdin").toString().trim().split("\n");

let bracket = input[0];

let stack = [];
let answer = 0;
let tmp = 1;

for (let i = 0; i < bracket.length; i++) {
    if (bracket[i] === "(") {
        stack.push(bracket[i]);
        tmp *= 2;
    } else if (bracket[i] === "[") {
        stack.push(bracket[i]);
        tmp *= 3;
    } else if (bracket[i] === ")") {
        if (!stack.length || stack[stack.length - 1] === "[") {
            answer = 0;
            break;
        }
        if (bracket[i - 1] === "(") {
            answer += tmp;
        }
        stack.pop();
        tmp /= 2;
    } else {
        if (!stack.length || stack[stack.length - 1] === "(") {
            answer = 0;
            break;
        }
        if (bracket[i - 1] === "[") {
            answer += tmp;
        }
        stack.pop();
        tmp /= 3;
    }
}

if (stack.length > 0) {
    console.log(0);
} else {
    console.log(answer);
}
