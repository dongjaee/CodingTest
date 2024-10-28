#1.이진수 변환
#2.해당 자리수에 있는거면 cnt+=1
    #cnt*# answer 어팬드


def solution(n, arr1, arr2):
    answer = []
    for a, b in zip(arr1, arr2):
        a = bin(a)[2:].zfill(n)
        b = bin(b)[2:].zfill(n)
        
        combined = ''.join(['#' if x == '1' or y == '1' else ' ' for x, y in zip(a, b)])
        
        answer.append(combined)
    
    return answer