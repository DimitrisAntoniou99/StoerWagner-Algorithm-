import sys


def Neighbors(E, node):
    N = []
    for e in E.keys():
        if (e[0] == node):
            N.append(e[1])
    return N


def BFS(V, E, s, t):
    d = dict()
    parents = dict()
    visited = set()
    for v in V:
        d[v] = float('inf')
    d[s] = 0
    parents[s] = None

    Q = [s]
    visited.add(s)
    while (len(Q) > 0):
        u = Q.pop(0)
        N = Neighbors(E, u)
        for v in N:
            if v not in visited:
                Q.append(v)
                visited.add(v)
                d[v] = d[u] + E[(u, v)]
                parents[v] = u

    if t not in parents.keys():
        return []

    path = []
    prev = t
    while (parents[prev] != None):
        u = parents[prev]
        v = prev
        path.insert(0, (u, v, E[(u, v)]))
        prev = u

    return path


def FordFulkerson(G, s, t):
    # Assumes that "s" will be the start and "t" is the target
    Gf = G[1]

    p = BFS(G[0], Gf, s, t)
    while len(p) > 0:
        # Least residual capactiy edge in p
        cap_p = min(p, key=lambda elem: elem[2])

        # Reconstruct the Residual Graph
        for ed in p:
            up_dict = dict()

            n = (ed[0], ed[1])
            val = Gf[n] - cap_p[2]
            if val == 0:
                Gf.pop(n)
            else:
                up_dict[n] = val

            rev_n = (ed[1], ed[0])
            if rev_n in Gf.keys():
                rev_val = Gf[rev_n] + cap_p[2]
            else:
                rev_val = cap_p[2]
            up_dict[rev_n] = rev_val
            Gf.update(up_dict)
        p = BFS(G[0], Gf, s, t)
    flow = []
    max_flow = 0
    for dge in Gf.keys():
        if dge[1] == s:
            flow.append((dge[1], dge[0], Gf[dge]))
            max_flow += Gf[dge]

    return (flow, max_flow)


if __name__ == "__main__":
    V = set()
    E = dict()
    with open("input48_1128.txt", 'r') as f:
        while True:
            new_edge = f.readline()
            if not new_edge:
                break
            edge = new_edge.split()
            V.add(edge[0])
            V.add(edge[1])
            E[(edge[0], edge[1])] = int(edge[2])
    G = (V, E)
    for i in V:
        s=''
        #x=input("Give a destination : ")
        t=i
        #print(s,t)
        r=FordFulkerson(G,s,t)
        #r_sorted = sorted(r[1], key=lambda x: x[1])
        #print("cut edges " + str(r_sorted))
        print(s,t,"maxflow value " + str(r[1]))
