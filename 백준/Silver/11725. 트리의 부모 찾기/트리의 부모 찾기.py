import sys

N = int(sys.stdin.readline().strip())  
tree = [[] for _ in range(N + 1)]
parent = [0] * (N + 1)

for _ in range(N - 1): 
    a, b = map(int, sys.stdin.readline().split())
    tree[a].append(b)
    tree[b].append(a)

stack = [1]
while stack:
    node = stack.pop()
    for next_node in tree[node]:
        if not parent[next_node]:  
            parent[next_node] = node  
            stack.append(next_node)  

for i in range(2, N + 1):
    print(parent[i])