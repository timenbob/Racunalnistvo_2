def razrez_palice(N,L):
    dat=dict()
    
    def fun(i,j):
        if j-i<=1:
            return 0
  
        if (i,j) not in dat:
            v=[]
            for k in range(i+1,j):
                v.append(fun(i,k)+fun(k,j))
            if v==[]:
                return 0
            else:
                dat[i,j]=min(v)+L[j]-L[i]
        else:
            return dat[i,j]
        
        
        
    return fun(0,N-1)

razrez_palice(10,[1,4,8])