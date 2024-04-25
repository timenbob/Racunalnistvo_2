from djikstra import djikstra
with open("C:\\Users\\tb9218\\Documents\\Racunalnistvo_2\\VAJE\\vaje9\\mesta.txt") as f:
    g={}
    mesta={}
    ind=0
    while True:
        line = f.readline()
        
        if not line:
            break
        mesto,_,_,_,d,_=line.split(",")
        mesta[mesto]=ind
        ind+=1

        g[mesta[mesto]]=[]
        
        for _ in range(int(d)):
            line=f.readline()
            sosed,_,radzalija=line.split(",")
            sosed=sosed.strip()
            g[mesta[mesto]].append((mesta[sosed],int(radzalija)))
            g[mesta[sosed]].append((mesta[mesto],int(radzalija)))
            
#print(g)

print(djikstra(g, 0))
print(mesta)        