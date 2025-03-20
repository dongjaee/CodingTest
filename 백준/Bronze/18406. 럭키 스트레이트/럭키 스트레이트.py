nums=list(str(input()))
s=0
e=0
for i in range(len(nums)):
    if i<len(nums)//2:
        s+=int(nums[i])
    else:
        e+=int(nums[i])
        
if s==e:
    print('LUCKY')
else:
    print('READY')