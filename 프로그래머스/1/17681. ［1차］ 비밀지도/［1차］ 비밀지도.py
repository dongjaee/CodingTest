def solution(n, arr1, arr2):
    answer = []
    for a, b in zip(arr1, arr2):
        a = bin(a)[2:].rjust(n,'0')
        b = bin(b)[2:].rjust(n,'0')
        
        combined = ''.join(['#' if x == '1' or y == '1' else ' ' for x, y in zip(a, b)])
        
        answer.append(combined)
    
    return answer