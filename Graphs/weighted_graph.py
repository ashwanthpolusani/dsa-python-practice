from collections import defaultdict

#        3
#   5---------2
#   | \ 1   / | \ 2
#   |  \   /  |  \
#  2|    X    |4  3
#   |  /   \  |  /
#   | / 2    \| / 3
#   7---------8
#         1
#

def all_paths(u,v,path=[],cost=0):
    path.append(u)
    if u==v:
        print(path,cost)
    else:
        for i,w in graph[u]:
            if i not in path:
                cost=cost+w
                all_paths(i,v,path,cost)
                cost=cost-w
        path.pop()
a=[(5,2,3),(5,7,2),(5,8,1),(2,7,2),(2,8,4),(2,3,2),(3,8,3),(8,7,1)]
graph = defaultdict(list)
for u,v,w in a:
    graph[u].append((v,w))
    graph[v].append((u,w))
print(graph)
all_paths(5,8)