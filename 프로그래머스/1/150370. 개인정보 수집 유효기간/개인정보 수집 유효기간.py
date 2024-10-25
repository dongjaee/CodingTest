#terms로 각각 길이 조건 뽑기
#1. privacies 길이만큼 반복문
#   길이 넘으면 끝
#   아니면 어펜드   


def solution(today, terms, privacies):
    answer = []
    terms = [i.split(' ') for i in terms]
    today_year,today_month,today_day=map(int,today.split('.'))
    
    for i in range(len(privacies)):
        past, term_type = privacies[i].split(' ')
        year, month, day = map(int, past.split('.'))
        
        for term in terms:
            if term_type == term[0]:  
                total_month = month + int(term[1])
                year += (total_month - 1) // 12  
                month = (total_month - 1) % 12 + 1 
                break  
        
        if (year < today_year) or \
           (year == today_year and month < today_month) or \
           (year == today_year and month == today_month and day <= today_day):
            answer.append(i + 1)
    
    return answer