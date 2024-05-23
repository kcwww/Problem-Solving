function combination(arr, selectNum) {
    const result = [];
    if (selectNum === 1) return arr.map((v) => [v]);
    arr.forEach((v, idx, arr) => {
        const fixed = v;
        const slicedArr = arr.slice(idx + 1);
        const resultArr = combination(slicedArr, selectNum - 1);
        const withFixed = resultArr.map((v) => [fixed, ...v]);
        result.push(...withFixed);
    });
    return result;
}

const checkAnswer = (arr, answer) => {
    for (const key of answer) {
        if (key.every(element => arr.includes(element))) {
            return false;
        }
    }
    return true;
}

function solution(relation) {
    let answer = [];
    
    // 순회하며 후보키 인덱스로 저장 o
    
    // 중복값일 경우 해당 값은 후보키에서 제외 o
    
    // 제외된 후보키들 끼리 조합해서 확인
    
    // 조합했을때도 저장 후 뒤의 경우 제외하기
    
    const relationObj = {};
    const result = {};
    const length = relation[0].length;
    
    for (let i = 0; i < length; i++) result[i] = true;
    relation.forEach((element) => {
        element.forEach((v, index) => {
            if (relationObj[index] === undefined) relationObj[index] = [];
            if (relationObj[index].includes(v)) result[index] = false;
            relationObj[index].push(v);
            
        })
    });
    
    const noRelation = [];
    Object.values(result).forEach((v, index) => {
        if (v) answer.push([index]);
        else noRelation.push(index);
    });
    
    const combinationArr = [];
    for (let i = 2; i < length; i++) combinationArr.push(...combination(noRelation, i));
    
    
    const rlength = relationObj[0].length;
    combinationArr.forEach((element) => {
        const obj = new Map();
        for (let i = 0; i < rlength; i++) {
            const str = element.reduce((acc, cur) => acc + relationObj[cur][i], '');
            if (obj.has(str)) {
                obj.set('no', -1);
                break;
            }
            else obj.set(str, true);
        }
        if (obj.get('no') === -1) return;
        
        if (checkAnswer(element, answer)) answer.push(element);
    })
    
    
    return answer.length === 0 ? 1 : answer.length;
}