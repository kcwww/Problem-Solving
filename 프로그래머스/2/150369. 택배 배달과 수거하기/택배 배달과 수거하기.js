
function findIdx(deliveries, pickups, n) {
  let i = n - 1;
  while (i >= 0) {
    if (deliveries[i] !== 0) break;
    i--;
  }
  let j = n - 1;
  while (j >= 0) {
    if (pickups[j] !== 0) break;
    j--;
  }
  return [i, j];
}

function findNextIdx(deliveries, pickups, i, j) {
  if (i !== -1) {
    while (i >= 0) {
      if (deliveries[i] !== 0) break;
      i--;
    }
  }

  if (j !== -1) {
    while (j >= 0) {
      if (pickups[j] !== 0) break;
      j--;
    }
  }
  return [i, j];
}

function delivery(deliveries, i, cap) {
  let volume = 0;
  while (i >= 0) {
    volume += deliveries[i];

    if (volume === cap) {
      deliveries[i] = 0;
      break;
    } else if (volume > cap) {
      deliveries[i] = volume - cap;
      break;
    } else {
      deliveries[i] = 0;
    }
    i--;
  }
  return i;
}

function pickup(pickups, j, cap) {
  let volume = 0;
  while (j >= 0) {
    volume += pickups[j];

    if (volume === cap) {
      pickups[j] = 0;
      break;
    } else if (volume > cap) {
      pickups[j] = volume - cap;
      break;
    } else {
      pickups[j] = 0;
    }
    j--;
  }
  return j;
}

function solution(cap, n, deliveries, pickups) {
  // 둘다 0 일때
  // 배달이 0이 아닐때 -> 시작 -> 거기까지는 무조건 가야함 -> 가면서 + 배달 + 내려오면서 수거
  // 수거가 0이 아닐때 -> 시작 -> 거기까지는 무조건 가야함 -> 가면서 배달 + 도착후 수거 + 내려오면서 나머지 수거
  // 둘다 0 이 아닐때 -> 시작 -> 거기까지는 무조건 가야함 -> 끝까지 가면서 배달 후 수거 하면서 오기
  // 배달만 있을수도 있고 수거만 있을수도 있음
  let distance = 0;
  let [i, j] = findIdx(deliveries, pickups, n);

  while (true) {
    if (i === -1 && j === -1) break;
    // 맨 끝지점 찾기
    if (i >= 0 || j >= 0) {
      const d = (i >= j ? i : j);
      distance += (d + 1) * 2;
    }

    // 배달 수거 로직
    if (i >= j) {
      i = delivery(deliveries, i, cap);
      j = pickup(pickups, j, cap);
    } else {
      j = pickup(pickups, j, cap);
      i = delivery(deliveries, i, cap);
    }
    [i, j] = findNextIdx(deliveries, pickups, i, j);
  }
  return distance;
}
