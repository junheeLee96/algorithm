function solution(friends, gifts) {
//     두 사람이 선물받은 기록 잇다 => 더 많이 준 사람이 선물 받음
//     두 사람이 기록이 없거나 주고받은 회수가 같다 => 선물 지수가 큰 사람이 선물 받음
//     선물 지수는 이번달까지 자신이 친구들에게 준 선물의 수 - 받은 선물의 수
//     선물지수도 같다면 주고받지 않음
    let obj = {}
    let cnt = {}
    for (let f of friends){
            obj[f] = [0,{}];
            cnt[f] = 0
    }
    for(let g of gifts){
        const [giver, rec] = g.split(' ');
        obj[giver][0] += 1;
        if(obj[giver][1][rec]){
            obj[giver][1][rec] += 1
        }else{
            obj[giver][1][rec] = 1
        }
        obj[rec][0] -= 1;
        if(obj[rec][1][giver]){
            obj[rec][1][giver] -= 1
        }else{
            obj[rec][1][giver] = -1
        }
    }
    
    
    for(let gi of friends){
        for(let gi2 of friends){
            if(gi === gi2) continue;
            if(obj[gi][1][gi2] > obj[gi2][1][gi]){
                cnt[gi] += 1
            }else if (obj[gi][1][gi2] === obj[gi2][1][gi] ){
                if(obj[gi][0] > obj[gi2][0]){
                    cnt[gi] += 1
                }
            }
        }
    }
    const arr = Object.entries(cnt);
    arr.sort((a,b)=> b[1]-a[1]);
    return arr[0][1]
}