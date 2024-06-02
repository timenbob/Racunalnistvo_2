# 4 poročilo za Računalništvo 2 
* Avtor : Timen Bobnar 
* Datum : 2.6.2024

## Povzetek

Na zadnjih treh vajah smo obravnavali 3 različne probleme. Prvi problem, ki ga bomo tudi predstavili, prikazuje uporabo dvojiške kopice. Drugi problem, ki smo se ga lotili, je iskanje minimalnega vpetega drevesa. To je problem, kjer iz osnovnega grafa vozlišč ter neusmerjenih, obteženih povezav izberemo tak podgraf, da vsebuje vsa vozlišča ter da je skupna cena povezav najmanjša. V zadnjem problemu smo reševali problem trgovskega potnika. To je problem, kjer imamo podan osnovni graf vozlišč in povezav. Želimo pa poiskati tako obhod, da obiščemo vsa vozlišča ter je skupna cena prepotovanih povezav minimalna. Računali smo kriterijsko funkcijo, ki nam poda oceno, koliko minimalno stanejo vse krožne povezave, ki vsebujejo nekatere povezave v našem grafu.

## Opis problema
Podano imamo podatkovno strukturo dvojiška kopica. Želimo si ogledati, kako ta struktura sploh deluje, kako deluje dodajanje ter brisanje elementov in nekaj uporab te strukture.

## Kopica
Kopica je levo poravnano dvojiško drevo, ki se deli na minimalno ter maksimalno kopico. Minimalna kopica pomeni, da je vrednost vozlišča manjša kot vrednost v otrocih. Iz te lastnosti sledi, da je najmanjša vrednost v naši minimalni dvojiški kopici v korenu. Dvojiška kopica ima tudi operacije Dodaj ter Izbriši.

### Operacije
Operacije bomo implementirali na minimalni kopici, seveda je implementacija za maksimalno kopico zelo podobna.
#### Dodaj
V našo minimalno dvojiško kopico bi želeli vstaviti element.

To naredimo tako, da element vstavimo na prvi prosti list (da ohranimo levo poravnano obliko drevesa). Sedaj ko smo vstavili element preverimo, ali je vstavljeni element večji od svojega očeta (ena od lastnosti kopice). V primeru, da je vstavljeni element manjši od očeta, ga moramo v tem primeru zamenjati z očetom. Ta postopek ponavljamo, dokler ni naš element na pravem mestu.
```
Vstavi 1
      0
     / \
    3   4
   /
  6  
```
```
      0
     / \
    3   4
   / \
  6   1
Preverimo lastnos ali je 1 večje od 3. Ni torej zamenjamo 1 in 3.
```
```
      0
     / \
    1   4
   / \
  6   3
Preverimo lastnos ali je 1 večje od 0. Je torej smo končali.
```
##### Časovna analiza
V najslabšem primeru moramo element prenesti od lista do korena. Torej moramo opraviti toliko primerjav kot je višina drevesa. Za $n$ vozlišč je višina drevesa $log(n)$(saj je drevo levo poravnano) torej je naša časovna analiza enak $O(log(n))$.

#### Odstrani
Iz naše minimalne dvojiške kopice bi želeli odstraniti element.

To naredimo tako, da koren nadomestimo najbolj desnim listom. Sedaj bomo vozlišče v korenu prestavljali v nižje nivoje. V primeru, da je naše vozlišče večje od vsaj enega od sinov, naše vozlišče zamenjamo z manjšim od sinov. To ponavljamo dokler se da.
```
odstrani
      0
     / \
    1   4
   / \
  6   3
```
```
      3
     / \
    1   4
   / 
  6   
3 postavimo namesto korena
```
```
      3
     / \
    1   4
   / 
  6   
ker je 3 manše od 4 vendar večje od 1 zamenjamo 1 in 3.
```
```
      1
     / \
    3   4
   / 
  6   
ker je 3 manše od 6(od vseh sinov) smo končali.
```
##### Časovna analiza
V najslabšem primeru moramo element prenesti od korena do lista. Torej moramo opraviti toliko primerjav, kot je višina drevesa. Za $n$ vozlišč je višina drevesa $log(n)$ torej je naša časovna analiza enak $O(log(n))$.

#### Programerska implementacija
Radi bi implementirali operaciji Dodaj ter Odstrani. To bomo naredili tako, da bomo našo dvojiško kopico implementirali s seznamom ter pravili (za i-ti element velja):
* levi otrok ima indeks 2i + 1
* desni otrok ima indeks 2i + 2
* starš ima indeks (i-1)//2 (zaokroženo navzdol oziroma celoštevilsko deljenje)
Lahko bi tudi samo uporabili knjižnico heapq, ki ima obe operaciji že implementirani( heappush in heappop)
###### Dobi starša
```Python
  dobi_strsa(T,i):
  """T je seznam elementov naše kopice"""
    Return T[(i-1)//2]
```
###### Dodaj
```Python
    dobi_strsa(T,i):
    """T je seznam elementov naše kopice"""
        Return T[(i-1)//2]

    dodaj(T,x):
    """T je seznam elementov naše kopice"""
        T.append(x)
        c=len(T)-1
        while dobi_starsa(T,c)>T[c]:
            T[(c-1)//2],T[c]=T[c],T[(c-1)//2]
            c=(c-1)//2

    izbrisi(T):
    """Izbrišemo koren"""
    koren=T[0]
    T[0]=T[len(T)-1]
    T.pop()
    c=0
    while True:
        node=None
        l,L=levi_otrok(T,c)"l je indeks otroka, L vrednost levega otroka"
        d,D=desni_otrok(T,c)
        if L<D and T[c]>L:
            node=(l,L)
        elif T[C]>D:
            node=(d,D)
        if !node:
            return root
        else:
            ind,val=node
            T[ind],T[c]=T[c],T[ind]
            c=ind
        
```
### Urejanje s kopico(heap sort)
Vse elemente neurejenega seznama dodamo v kopico. Sedaj imamo v korenu najmanjši element. Torej ga dodamo v urejeno vrsto, kopica se uredi in imamo spet v korenu najmanjši element. Ponavljamo, dokler še imamo kakšen element v kopici.
#### časovna analiza
Ker potrebujemo najprej $n$ vstavljanj in na to $n$ odstranjevanj je torej časovna analiza $$O(n*log(n)+n*log(n))=O(n*log(n))$$
#### Uporabnost
Urejanje s kopico je zelo uporabno, saj je zelo preprost način urejanja, zelo učinkovit ter časovna analiza je zmeraj $O(n*log(n))$
Slabost je le ta, da ne moremo uporabljati paralelnih algoritmov.

### Zlivanje $k$ urejenih seznamov
Iz vsakega od $k$ urejenih seznamov vzamemo po en element (prvi) in sestavimo kopico. Sedaj iz kopice odstranimo koren in ga damo v urejen seznam. Hkrati dodamo nov element v kopico, in sicer naslednji v vrsti, tisti izmed $k$ urejenih seznamov, iz katerega prihaja element, ki smo ga odstranili.

```
[1,3,4]
[0,5,6]
[7,8]
```
```
odstranimo vse prve in naredimo derevo
[3,4]    0
[5,6]   / \
[8]    1   7
```
```
odstranimo koren in dodamo 5
[3,4]    1
[6]     / \
[8]    7   5
Rešitev=[0]
```
```
odstranimo koren in dodamo 3
[4]      3
[6]     / \
[8]    7   5
Rešitev=[0,1]
```
```
odstranimo koren in dodamo 4
[]       4
[6]     / \
[8]    7   5
Rešitev=[0,1,3]
```
```
odstranimo koren in ne dodamo nič ker je prvi seznam prazen
[]       5
[6]     / 
[8]    7   
Rešitev=[0,1,3,4]
```
```
odstranimo koren in dodamo 6
[]       6
[]      / 
[8]    7   
Rešitev=[0,1,3,4,5]
```
odstranimo koren in ne dodamo nič
[]      7 
[]      
[8]      
Rešitev=[0,1,3,4,5,6]
```
odstranimo koren in dodamo 8 
[]      8 
[]      
[]      
Rešitev=[0,1,3,4,5,6,7]
```
odstranimo koren in ne dodamo nič
[]       
[]      
[]      
Rešitev=[0,1,3,4,5,6,7,8]
```
#### Časovna analiza
$k$ naj bo število seznamov ter $n$ število vseh elementov. 
$$O(n*k*log(k))$$

### Primeru uporabe 
Kot smo že opazili, se kopica lahko uporablja za hranjenje podatkov in urejevanje teh podatkov.
Nekatere druge uporabnosti:
* Kopice se uporabljajo za razporejanje dogodkov v simulacijskih sistemih, kjer je pomembno hitro najti naslednji dogodek, ki se mora zgoditi.
* V algoritmu Dijkstra se kopice uporabljajo za učinkovito iskanje naslednjega vozlišča z najkrajšo trenutno znano razdaljo.
* Kopice se uporabljajo za učinkovito implementacijo prednostnih vrst, kjer elementi z višjo prednostjo pridejo na vrsto pred elementi z nižjo prednostjo. Kopice omogočajo hitro vstavljanje novih elementov in hitro pridobivanje elementa z najvišjo prednostjo.
* Dve kopici (max-heap in min-heap) se uporabljata za učinkovito vzdrževanje trenutne mediane toka podatkov.

### Mnenje
Vaje so mi zelo všeč, saj skupaj analiziramo probleme. 

### Viri
Zapiski iz vaj
ChatGPT