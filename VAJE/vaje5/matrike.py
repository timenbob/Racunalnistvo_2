def zaporedje_matrike(dims):    
    """
    Funkcija izračuna število operacij pri optimalnem produktu matrik A_1*A_2*...A_n,
    kjer so dimenzije matrike A_i enake dims[i-1] x dims[i].
    """
    n = len(dims)

    # Pripravimo si tabelo velikost n x n. N[i][j] nam bo predstavljalo
    # najbolj ugodno množenje matrik A[i] * ... * A[j]
    N = [[0]*n for _ in range(n)]  
    
    for st_matrik in range(2, n):
        # zmnožimo skupaj prvih st_matrik in vzamemo najbolj ugodno možnost
        for i in range(1, n-st_matrik + 1):
            j = i + st_matrik-1

            # Izračunamo najbolj ugodno množenje matrik A[i] * ... A[j]           
            N[i][j] = min((N[i][k] + N[k+1][j] + dims[i-1]*dims[k]*dims[j] for k in range(i, j)))   
    
    
    
    return N[1][n-1]


## Primer uporabe. Odkomentiraj spodnje vrstice in poženi program

# dimenzije = [3,3,4,4,5,5,3,3,5,4,13,2,6,5,4]
# print(f"Optimalno število operacij za produkt je {zaporedje_matrike(dimenzije)}")