def solution(food):
    result=[]
    answer=''
    for i in range(1,len(food)):
        result.append(food[i]//2)
    
    for a,b in enumerate(result):
        num = a + 1
        answer += str(num) * b
            
            
    answer=answer+'0'+answer[::-1]
    return answer