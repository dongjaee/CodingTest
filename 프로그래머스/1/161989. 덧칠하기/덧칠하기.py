def solution(n, m, section):
    answer = 0
    painted = 0  
    
    for s in section:
        if painted < s:
            painted = s+m-1 
            answer += 1
    
    return answer