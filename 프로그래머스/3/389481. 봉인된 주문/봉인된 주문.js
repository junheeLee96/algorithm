function solution(n, bans) {
    var answer = '';
    const Base26Arr = bans.map(ToBase26).sort((a,b)=>a-b);
    let target = n;
    
    for(let Base26 of Base26Arr){
        if (Base26 <= target){
            target ++;
        }else{
            break;
        }
    }
    answer = ToNumber(target)
    return answer;
}

function ToBase26(char){
    let result = 0;
    
    for(let c of char){
        let num = c.charCodeAt(0) - 'a'.charCodeAt(0) + 1;
        result = result * 26 + num;
    }
    return result;
}
function ToNumber(num) {
    let str = '';

    // 숫자가 0보다 큰 동안 반복
    while (num > 0) {
        // 'a'부터 시작해서 num-1의 나머지 값으로 문자 계산
        let c = String.fromCharCode('a'.charCodeAt(0) + (num - 1) % 26);
        str += c;  // 문자를 str에 추가
        num = Math.floor((num - 1) / 26);  // num을 26으로 나눈 몫으로 갱신
    }

    // 결과는 뒤집어서 반환해야 하므로, reverse()로 반전시켜 반환
    return str.split('').reverse().join('');
}
