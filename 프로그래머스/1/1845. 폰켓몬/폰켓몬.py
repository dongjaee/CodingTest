def solution(nums):
    dic=dict()
    for i in nums:
        if i in dic:
            dic[i]+=1
        else:
            dic[i]=1
        
    return len(dic.keys()) if len(dic.keys())<=len(nums)/2 else len(nums)/2