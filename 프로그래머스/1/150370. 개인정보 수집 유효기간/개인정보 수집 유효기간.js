function solution(today, terms, privacies) {
    var answer = [];
    
//     A => 6달
//     B => 12달
//     C => 3달
    let [t_year, t_month, t_day] = today.split('.').map(Number);
    let now =( t_year * 12 * 28 ) + (28 * t_month) + t_day;
    
    let obj = {}
    
    for(let t of terms){
        const [type,m] = t.split(' ');
        obj[type] = parseInt(m) * 28;
    }
    console.log(obj)
    
    for(let  i=0; i < privacies.length; i ++){
        let [date, type] = privacies[i].split(' ');
        let [year,month,day] = date.split('.').map(Number);
        const priv_day = (year * 12 * 28) + (month * 28) + day + obj[type];
        if (priv_day <= now){
            answer.push(i+1)
        }
    }
    return answer;
}