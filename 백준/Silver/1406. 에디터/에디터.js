let input = require("fs").readFileSync("/dev/stdin").toString().trim().split("\n");

const str = input[0];

let first = {
  value : input[0][0],
  next : null,
  prev : null
};

let current = first;

for (let i = 1; i < str.length; i++) {
  const node = {
    value : input[0][i],
    next : null,
    prev : null
  }
  node.prev = current;
  current.next = node;
  current = node;
}

input = input.slice(2);

input.forEach((e) => {
  const [N, M] = e.split(" ");

  if (N === "L") {
    if (current.prev !== null) current = current.prev;
    else if (current === first && current.value !== "") {
      const node = {
        value : "",
        next : current,
        prev : null,
      }
      first.prev = node;
      current = node;
      first = node;
    }
  } else if (N === "D") {
    if (current.next !== null) current = current.next;
  } else if (N === "P") {
    const node = {
      value : M,
      next : null,
      prev : null
    }

    if (current.value === "") {
      current.value = M;
    } else {
      node.prev = current;
      node.next = current.next;
      if (current.next !== null) current.next.prev = node;
      current.next = node;
      current = node;
    }
  } else if (N === "B") {
    if (current === first) {
      current.value = "";
    } else if (current !== null) {
      const temp = current.next;
      const temp2 = current.prev;
      if (temp2) temp2.next = temp;
      if (temp) temp.prev = temp2;
      current = current.prev;
    }
  }
});

let result = "";

while (first) {
  result += first.value;
  first = first.next;
}

console.log(result);
