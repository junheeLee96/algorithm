import datetime
from dateutil.relativedelta import relativedelta

def solution(today, terms, privacies):
    answer = []
    format = '%Y-%m-%d'
    dict = {}
    today = today.replace('.','-')
    dt_datetime = datetime.datetime.strptime(today,format)
    
    for i in terms:
        a,b = i.split()
        dict[a] = int(b)
    
    for i in range(len(privacies)):
        a , b= privacies[i].split()
        # b = int(b)
        
        p_day = a.replace('.','-')
        p = datetime.datetime.strptime(p_day,format)
        # pday = p+datetime.timedelta(days=dict[b] * 28)
        plus = p + relativedelta(months=dict[b])
        print(plus)
        if plus <= dt_datetime:
            answer.append(i+1)
        
    
    
    return answer