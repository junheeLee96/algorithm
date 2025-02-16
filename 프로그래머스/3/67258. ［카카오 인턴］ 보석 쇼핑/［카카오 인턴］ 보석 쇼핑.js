function solution(gems) {
    var answer = [0, gems.length];
    let obj = {};
    const length = new Set(gems).size; // 보석 종류 개수
    let kindCount = 0; // 현재 포함된 보석 개수
    
    let left = 0, right = 0;
    obj[gems[0]] = 1;
    kindCount = 1;

    while (left <= right && right < gems.length) {
        if (kindCount === length) {  // 모든 보석을 포함하는 경우
            if (answer[1] - answer[0] > right - left) {
                answer = [left + 1, right + 1];
            }
            
            obj[gems[left]] -= 1;
            if (obj[gems[left]] === 0) { // 보석 개수가 0이 되면 종류 감소
                delete obj[gems[left]];
                kindCount--;
            }
            left++;
        } else { // 모든 보석을 포함하지 못한 경우
            right++;
            if (right === gems.length) break;
            
            if (obj[gems[right]]) {
                obj[gems[right]] += 1;
            } else {
                obj[gems[right]] = 1;
                kindCount++; // 새로운 보석 추가될 때만 증가
            }
        }
    }

    return answer;
}
