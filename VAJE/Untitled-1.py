def printMatrix(M, dim):
    for i in range(dim):
        print(M[i])
def floyer(connections):
    # [(1, 3, weight)]
    dim = max([max(x, y) for x, y, _ in connections])

    con = [[None for i in range(dim)] for j in range(dim)]
    for x, y, w in connections:
        con[x-1][y-1] = w

    D = [[0 if i == j else float("inf") for i in range(dim)] for j in range(dim)]
    P = [[None for i in range(dim)] for j in range(dim)]

    for i in range(dim):
        for j in range(dim):
            if con[i][j] != None:   
                P[i][j] = i
                D[i][j] = con[i][j]

    for k in range(dim):
        for i in range(dim):
            for j in range(dim):
                prev = D[i][j]
                D[i][j] = min(D[i][j], D[i][k] + D[k][j])
                if prev > D[i][j]:
                    P[i][j] = k
    print("--"*20)
    printMatrix(D, dim)
    print("--"*20)
    printMatrix(P, dim)

def shortestPath(P, i, j):
    lst = [j]
    prev = j
    while True:
        if i == P[i][prev] or P[i][prev] == None:
            return lst
        lst.append(P[i][prev])
        prev = P[i][prev]
        

example = [(1, 2, 4), (2, 4, 3), (1, 3, 4)]
floyer(example)