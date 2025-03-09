from collections import deque

N,K = map(int,input().split())

q=deque()
q.append((N,0))
visited=[False]*100001


while q:
    now,time=q.popleft()

    if now==K:
        print(time)
        break

    for i in (now+1,now-1,now*2):
        if 0 <=i<= 100000 and not visited[i]:
                visited[i] = True 
                q.append((i, time + 1))  