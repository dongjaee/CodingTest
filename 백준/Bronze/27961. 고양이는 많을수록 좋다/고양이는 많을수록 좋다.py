N=int(input())

result=0
cnt=0

while result<N:
    if result==0:
        result+=1
    else:
        if N-result<result:
            result+=N-result
        else:
            result+=result

    cnt+=1

print(cnt)