import numpy as np


def dfs(ford, flow_matrix, s, e):
    stack = [s]
    paths = {s: []}
    if s == e:  # if start is the same as end
        return paths[s]
    while stack:  # works until no vertices left on stack
        u = stack.pop()
        for v in range(len(ford)):
            if (ford[u][v] - flow_matrix[u][v] > 0) and v not in paths:  # if any flow possibility left and vertex 'v' not visited
                paths[v] = paths[u] + [(u, v)]  # path to current vertex 'v' equals path to his predecessor 'u' and edge from 'u' to 'v'
                print(paths)
                if v == e:  # if have reached the end node
                    return paths[v]
                stack.append(v)
    return None


def max_flow(ford, s, t):
    n = len(ford)
    flow_matrix = [[0] * n for i in range(n)]  # matrix describing current flow
    path = dfs(ford, flow_matrix, s, t)
    while path is not None:  # works until dfs returns none (no more paths in graph left)
        flow = min(ford[u][v] - flow_matrix[u][v] for u, v in path)  # choosing the lowest flow in path
        for u, v in path:  # saving counted flow in flow_matrix
            flow_matrix[u][v] += flow  # flow from vertex 'u' to 'v'
            flow_matrix[v][u] -= flow  # flow from vertex 'v' to 'u'
        path = dfs(ford, flow_matrix, s, t)
    return sum(flow_matrix[s][i] for i in range(n))  # return amount of outgoing flows from starting vertex (same amount has to flow into the ending vertex)


def main():
    f = open("ford.txt", 'r')
    content = f.read()

    # convert file content to 2-dimensional np.array
    temp_list = content.split("\n")  # list of strings, each string represent row in adjacency_matrix
    ford = np.empty((len(temp_list), len(temp_list)), dtype=int)  # set suitable dimensions
    for row in range(len(temp_list)):
        elements_in_row = list(map(int, temp_list[row].split(',')))  # converts string into list of strings, then converts strings into integers
        for element in range(len(elements_in_row)):  # sets elements on its positions in adjacency_matrix
            ford[row, element] = elements_in_row[element]

    print("Ford-Fulkerson algorithm")
    begin = 0  # beginning vertex index
    end = ford.shape[0] - 1  # ending vertex index
    max_flow_value = max_flow(ford, begin, end)
    print("max_flow_value is: ", max_flow_value)

    f.close()


if __name__ == '__main__':
    main()