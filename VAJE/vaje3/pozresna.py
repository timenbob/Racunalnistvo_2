def pozresna(predmeti, W):
    novi=[]
    for el in predmeti:
        novi.append((el[0]/el[1],el[0],el[1]))
    novi.sort(key = lambda x:-x[0])
    opt=0
    v=W
    for el in novi:
        if v - novi[2]>0:
            v-=novi[2]
            opt+=novi[1]
    
    return opt

pozresna([(2,3), (4,4), (5,4), (3,2), (1,2), (15, 12)], 7)