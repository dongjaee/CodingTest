def solution(n):
    for i in range(n+1,1,-1):
        if n%i==1:
            result=i
        else:
            continue
    return result