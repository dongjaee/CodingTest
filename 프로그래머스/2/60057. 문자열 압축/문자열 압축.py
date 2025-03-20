def solution(s):
    if len(s) == 1:
        return 1  

    min_length = float('inf')  
    
    for step in range(1, len(s)//2 + 1):  
        compressed = ""
        prev = s[:step]  
        count = 1 

        for i in range(step, len(s), step):
            curr = s[i:i+step]  
            if curr == prev:
                count += 1  
            else:
                compressed += (str(count) if count > 1 else '') + prev  
                prev = curr  
                count = 1  
        
        compressed += (str(count) if count > 1 else '') + prev  
        min_length = min(min_length, len(compressed)) 

    return min_length