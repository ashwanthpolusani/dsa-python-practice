# given a graph and 2 nodes . find all paths between them

from collections import defaultdict
def all_paths(u,v,path=[]):
    path.append(u)
    if u==v:
        print(path)
    else:
        for i in d[u]:
            if i not in path:
                all_paths(i,v,path)
    path.pop()
    return

def Count_of_paths(u,v,path=set(),c=[0]):
    path.add(u)
    if u==v:
        c[0] += 1
    else:
        for i in d[u]:
            if i not in path:
                Count_of_paths(i,v,path,c)
    path.remove(u)
    return c[0]
def validpath(u,v,path=set()):
    path.add(u)
    if u==v:
        return True
    else:
        for i in d[u]:
            if i not in path:
                if validpath(i,v,path):
                    return True
    return False

def validpathbfs(u):
    v={u}
    q=[u]
    while q:
        curr =q.pop()
        print(curr)
        for i in d[curr]:
            if i not in v and i not in q:
                v.add(i)
                q.append(i)

if __name__=="__main__":
    graph=[[5,2],[5,7],[5,8],[2,3],[2,8],[2,7],[7,8],[8,3]]
    d=defaultdict(list)
    for i,j in graph:
        d[i].append(j)
        d[j].append(i)
    # print(d)
    # all_paths(5,3)
    # print(Count_of_paths(5,3))
    print(validpath(5,3))
    print(validpathbfs(5))