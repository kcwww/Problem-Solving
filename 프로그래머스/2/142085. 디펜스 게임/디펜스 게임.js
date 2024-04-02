function solution(n, k, enemy) {
    let lt = 0, rt = enemy.length;

    while(lt <= rt) {
        let mid = Math.floor((lt+rt) / 2);
        if(check(n, k, mid, enemy)) lt = mid+1;
        else rt = mid - 1;
    }

    return lt - 1;
}

const check = (n, k, mid, enemy) => {
    if (mid <= k) return true;

    let t = enemy.slice(0, mid).sort((a, b) => b - a);
    let sum = 0;

    for (let i = k; i < t.length; i++) {
        sum += t[i];
        if (sum > n) return false;
    }
    return true;

}