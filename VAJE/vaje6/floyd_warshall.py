def floyd_warshall(povezave):
    n=len(povezave)
    D= [list(range(1 + n * i, 1 + n * (i + 1))) for i in range(n)]
    P= [list(range(1 + n * i, 1 + n * (i + 1))) for i in range(n)]
    for i in range(n):
        for j in range(n):
    
    