def solution(friends, gifts):
    n=len(friends)
    field=[[0]*n for _ in range(n)]
    
    for i in gifts:
        give,take=i.split()
        field[friends.index(give)][friends.index(take)] += 1
    
    
    given=[sum(i) for i in field]
    received = [sum(field[j][i] for j in range(n)) for i in range(n)] 
    gift_index = [given[i] - received[i] for i in range(n)]
    
    result=[0]*n
    
    for i in range(n):
        for j in range(n):
            if i==j:
                continue
                
            if field[i][j] > field[j][i]:  
                result[i] += 1
            elif field[i][j] == field[j][i]:  
                if gift_index[i] > gift_index[j]:  
                    result[i] += 1

    return max(result)
    

