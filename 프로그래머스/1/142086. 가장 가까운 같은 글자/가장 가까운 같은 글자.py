def solution(s):
    str = list(s)
    answer=[-1]
    for i in range(2,len(str)+1):
        for j in range(i-1,0,-1):
            if str[i-1]==str[j-1]:
                answer.append(i-j)
                break
        else:
            answer.append(-1)
    return answer