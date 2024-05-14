## Poročilo za Računalništvo 2 - matrično množenje in najdaljša naraščajoča/padajoča pod zaporedja
* Avtor : Timen Bobnar 
* Datum : 6.4.2024

### Povzetek

Na vajah smo obdelali dve vrsti problemov matrično množenje ter najdaljša pod zaporedja.\
Ko smo obdelovali primere iz matričnega množenja smo najprej predstavili kakšni so vhodni podatki in ustvarili Bellmanovo enačbo, ki izračuna minimalno število množenj. Ogledali smo si delovanje funkcije Zaporedje matrik, ki vrne v kakšne zaporedju moramo množiti matrike. Preostanek vaj je bil namenjen programiranju 2h problemov

*  st_ optimalnih produktov
* optimalni produkti

Na vajah iz pod zaporedij smo najprej ponovili kaj zares je naš problem napisali Bellmanovo enačbo ter nato rešili naslednje 3 probleme:
* zanima nas dolžina najdaljšega padajočega pod zaporedja
* zanima nas še dejansko po dzaporedje
* zanima nas število najdaljših podz aporedij

Na koncu smo reševali še naloge na TOMO-tu.

### Opis problema
Obdelovali bomo problem iskanja najdaljšega strogo naraščajočega pod zaporedja.
Vhodni in izhodni podatek sta seznama števil. Veljajo pravila elementi v izhodnem seznamu recimo mu M so v enakem vrstnem redu kot podatki v vhodnem seznamu recimo mu N. V enakem vrsten redu je mišljeno, da lahko izpustimo kakšen element.

Vhod:\
$N=[5,1,8,3, 8, 3, 9, 8, 2 ,12, 11, 5 ,6 ,7]$\
Izhod:\
$M=[1, 3, 8, 9, 12]$\
druge možnosti ${[1,3,8,9,11],[1,3,5,6,7],[1,2,5,6,7],\dots}$ 


#### Bellmanova enačba za dolžino najdaljšega zaporedja
Vhod seznam $N$\
Bellmanova enačba $$l(i)=max_{(j=0)and(N(j)<N(i))}^{i-1} l(j)+1$$
Ustavitveni pogoj $$l(0)=1 $$
Kjer $l(i)$ predstavlja dolžino najdaljšega naraščajočega pod zaporedja, ki se konča z elementom $N(i)$. Imamo še pogoj $(N(j)<N(i))$, ki je tu za to, da omejimo vse možne izbire elementov iz N-ja, omejimo se na elemente manjše od N(i).

#### Ustvarjanje najdaljšega pod zaporedja
V zgornji Bellmanovi enačbi $l(i)$ predstavlja najdaljše naraščajoče pod zaporedje, ki se konča z elementom $N(i)$, opazimo, da na tak način imamo že podan en element našega seznama in sicer zadnji element. Da pridobimo ostale elemente, potrebujemo predhodnika i-tega elementa. Saj, če imamo dostop do predhodnika za vsak $i$ pomeni, da imamo dostop do vseh predhodnikov. Predhodnika bomo označili s $P(i)$. $P(i)$ nam pove indeks od predhodnega elementa z indeksom $i$ (v seznamu za $N$).

#### Kako izračunati $P(i)$
$P(i)$ nam pove indeks od predhodnega elementa z indeksom $i$ ( v seznamu $N$). Torej $predhodnik elementa $N(i)$ je element na mestu $N(P(i))$. Indeks predhodnika lahko pridobimo iz Bellmanove enačbe in sicer kjer je dosežen maksimum za $l(i)$. Torej potrebujemo postopek kako pridobiti indeks iz $max_{(j=0)and(N(j)<N(i))}^{i-1} l(j)$. Maksimum nam vrne maksimalno dolžino pod zaporedij, ki se konča z $N(i)$. Preko indeksiranja v maksimumu bomo v $P(i)$ shranili indeks kjer je dosežen maksimum. Če takega indeksa ni potem je $P(i) == None$

#### Izpis zaporedja

V tem trenutku imamo ustvarjen celoten seznam $P$. Sedaj da ustvarimo še zaporedje, se držimo le formule:
$$[\dots,N(P(P(i))),N(P(i)),N(i)]$$
Na tak način ustvarimo naše zaporedje, ki se konča z elementom N(i).

### Mnenje
Vaje so mi zelo všeč, saj skupaj analiziramo probleme. 

### Viri
Zapiski iz vaj.