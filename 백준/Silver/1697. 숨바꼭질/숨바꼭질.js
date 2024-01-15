let input = require("fs").readFileSync("/dev/stdin").toString().trim().split("\n");

const [start, destination] = input[0].split(" ").map(v => +v);



const solution = (start, destination) => {
  if (start === destination) return 0;
  let time = 0;


  const q = {
    time : 0,
    place : start
  };

  const total = {};
  total[start] = time;

  const queue = [q];

  while (queue.length) {
    const {place, time} = queue.shift();

    if (place === destination) break;

    let newPlace;
    if (place > destination) newPlace = [place - 1];
    else if (place <= 0) newPlace = [place + 1];
    else newPlace = [place + 1, place - 1, place * 2];

    newPlace.forEach((e) => {
      if (total[e] === undefined) {
        total[e] = time + 1;
        const obj = {
          time : time + 1,
          place : e
        }
        queue.push(obj);
      }
    });
  }
  return total[destination];
};


console.log(solution(start, destination));
