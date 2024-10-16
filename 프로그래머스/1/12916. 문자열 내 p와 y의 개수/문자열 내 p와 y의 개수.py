def solution(s):
    count_p,count_y=0,0
    
    for i in s.lower():
        if i=='p':
            count_p+=1
        if i=='y':
            count_y+=1
    
    if count_p==count_y:
        vaild=True
    else:
        vaild=False

    return vaild