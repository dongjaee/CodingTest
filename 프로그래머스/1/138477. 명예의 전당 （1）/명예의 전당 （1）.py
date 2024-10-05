def solution(k, score):
    arr = []
    answer = []
    
    for i in range(len(score)):
        if len(arr) < k:
            arr.append(score[i])
        else:
            if min(arr) < score[i]:
                arr.append(score[i])
                arr.sort(reverse=True)
                arr.pop()
        
        answer.append(min(arr))
    
    return answer