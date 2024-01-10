from collections import defaultdict
from collections import deque

INF = 999999999


def bfs(dag, cap, s, d):
    seen = defaultdict(lambda: False)
    prev = defaultdict(lambda: '')
    Q = deque()
    Q.append(s)
    seen[s] = True
    while Q:
        u = Q.popleft()
        for v in dag[u]:
            if (not seen[v]) and cap[(u, v)] > 0:
                Q.append(v)
                seen[v] = True
                prev[v] = u
                if v == d: break
    u = d
    path_cap = INF
    while u != '':
        path_cap = min(path_cap, cap[(prev[u], u)])
        u = prev[u]
    u = d
    while u != '':
        cap[prev[u], u] -= path_cap
        cap[u, prev[u]] += path_cap
        u = prev[u]

    return 0 if path_cap == INF else path_cap


def ford_fulkerson(dag, cap, s, d):
    max_flow = 0
    while True:
        pc = bfs(dag, cap, s, d)
        if pc == 0:
            break
        else:
            max_flow += pc
    return max_flow


'''
graph from http://community.topcoder.com/tc?module=Static&d1=tutorials&d2=maxFlow
input.txt:
7 8
X A 3
X B 1
A C 3
B C 5
B D 4
C Y 2
D E 2
E Y 3
main:
'''
f = open('../input48_1128.txt')
dag = defaultdict(list)
cap = defaultdict(lambda: INF)
V,E = map(int,f.readline().split())
for e in range(E):
    u,v,c = f.readline().split()
    dag[u].append(v)
    cap[(u,v)] = int(c)
print(ford_fulkerson(dag,cap,'0','11'))
print(ford_fulkerson(dag,cap,'1','3'))
