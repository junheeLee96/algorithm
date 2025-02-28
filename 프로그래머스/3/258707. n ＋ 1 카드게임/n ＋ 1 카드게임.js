function solution(coin, cards) {
    var answer = 0;
    const n = cards.length + 1;
    let hand = {};
    cards.splice(0, n / 3).forEach(v=> hand[v]=true);
    let keep = {};
    
    let round = 0;
    while(cards.length){
        cards.splice(0,2).forEach(v=> keep[v] = true);
        
        let pair = getPair(hand, n);
        if(pair){
            pair = parseInt(pair)
            delete hand[pair];
            delete hand[n - pair];
            round ++;
            continue;
        }
        let onePair = getOnePair(hand,keep,n)
        if(onePair && coin > 0){
            coin --;
            round ++;
            delete hand[parseInt(onePair)];
            delete keep[n - parseInt(onePair)];
            continue;
        }
        
        let twoPair = getPair(keep,n);
        if(twoPair && coin >=2 ){
            twoPair = parseInt(twoPair)
            coin -= 2;
            round ++;
            delete keep[twoPair];
            delete keep[n - twoPair];
            continue;
        }
        break;
    }
    
    
    return round + 1;
}

function getOnePair(hand,keep,n){
    for(let key in hand){
        if (keep[n - parseInt(key)]){
            return key
        }
    }
    return null
}

function getPair(hand,n){
    for(let key in hand){
        const target = n - parseInt(key);
        if(hand[target]){
            return key
        }
    }
    
    return null
}