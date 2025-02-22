function solution(users, emoticons) {
    var answer = [0,0];
    let sales = [10,20,30,40];
    const all = product(sales, emoticons.length);
    for(let sale of all){
        let total = [0,0] //플러스, 가격
        for(let user of users){
            let user_total = 0;
            for(let i =0; i < emoticons.length; i ++){
                if(sale[i] >= user[0]){
//                     유저가 사려는 세일이 더 높은 경우 => 사야함
                    // let price = emoticons[i] * (sale[i] / 100)
                    let price = emoticons[i] * ((100 - sale[i]) / 100);
                    user_total += price;
                    if(user_total >= user[1]) break;
                }
            }
            if(user_total >= user[1]){
//                 플러스 가입
                total[0] += 1
            }else{
                total[1] += user_total
            }
        }
        if(answer[0] < total[0]){
            answer = [...total]
        }else if (answer[0] === total[0] && answer[1] < total[1]){
            answer = [...total]
        }
    }
    return answer;
}
function product(arr, repeat) {
    return Array.from({ length: repeat })
        .reduce(acc => acc.flatMap(a => arr.map(b => [...a, b])), [[]]);
}