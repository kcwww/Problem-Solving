function solution(numbers) {
    const n = numbers.length;
    const answer = new Array(n).fill(-1);
    const stack = [];

    for (let i = n - 1; i >= 0; i--) {
        while (stack.length > 0 && numbers[stack[stack.length - 1]] <= numbers[i]) {
            stack.pop();
        }
        if (stack.length > 0) {
            answer[i] = numbers[stack[stack.length - 1]];
        }
        stack.push(i);
    }

    return answer;
}
