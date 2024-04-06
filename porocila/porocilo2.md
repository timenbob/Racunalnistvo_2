## Poročilo za Računalništvo 2 - matrično množenje in najdaljša naraščajoča/padajoča podzaporedja
* Avtor : Timen Bobnar 
* Datum : 6.4.2024

### Povzetek

Na vajah smo obdelali dve vrsti problemov matrično množenje ter najdaljša podzaporedja.\
Ko smo obdelovali primere iz matričnega množenja smo najprej predtsvili kakšni so vhodni podatki in ustavrili Bellmanovo enačbo, ki izračuna minimalno število množenj. Ogledali smo si delovanje funkcije Zaporedje matrik, ki vrne v kakšne zaporedju moramo množiti matrike. Preostanek vaj je bil namenjen programirnaju 2h problemov

*  st_ optimalnih_produktov
* optimalni produkti

Na vajah iz podzaporedij smo najprej ponovili kaj zares je naš problem napisali Bellmanovo enačbo ter nato rešili naslednje 3 probleme:
* zanima nas dolžina najdaljšega padajočega podzaporedja
* zanima nas še dejansko podzaporedje
* zanima nas število najdaljših podzaporedij

Na koncu smo reševali še naloge na TOMO-tu.

### Opis problema
Obdelovali bomo problem iskanja najdaljšega strogo naraščajočega podzaporedja.
Vhodni in izhodni podatek sta seznama števil. Velja par pravil elementi v izhodnem seznamu recimo mu M so v enakem vrstnem redu kot podatki v vhodnem seznamu recimo mu N. V enakem vrsten redu je mišljeno, da lahko izpustimo kakšen element.


Vhod:\
$N=[5,1,8,3, 8, 3, 9, 8, 2 ,12, 11, 5 ,6 ,7]$\
Izhod:\
$M=[1, 3, 8, 9, 12]$\
druge možnosti ${[1,3,8,9,11],[1,3,5,6,7],[1,2,5,6,7],\dots}$ 


#### Bellmanova enačba za dolžino najdaljšega zaporedja
Vhod seznam $N$\
Bellmanova enačba $$l(i)=max_{(j=0)and(N(j)<N(i))}^{i-1} l(j)+1$$
Ustavitveni pogoj $$l(0)=1 $$
Kjer $l(i)$ predtsvlja dožino najdaljšega naraščajočega podzaporedja, ki se konča z elementom $N(i)$. Imamo še pogoj $(N(j)<N(i))$ ki je tu za to, da omejimo vse možne izbire elementov iz N-ja, omejimo se na elemente manjše od N(i).

#### Generiranje najdaljšega podzaporedja
V zgornji Bellmanovi enačbi $l(i)$ predtsvljam najdaljše naraščajoče podzaporedje, ki se konča z elementom $N(i)$, opazimo da na tak način imamo že podan en element našega seznama in sicer zadnji element. Da pridobimo ostale elemenete potrebujemo predhodnika i-tega elementa. Saj, če imamo dostop do predhodnika za vask $i$ pomeni, da imamo dostop do vseh predhodnikov. Predhodnika bomo označili z $P(i)$. $P(i)$ nam pove indeks od predhodnega elementa z idneksom $i$ (v seznamu za $N$).

#### Kako izračunati $P(i)$
$P(i)$ je indeks predhodnika elementa $N(i)$. Torej $predhodnik N(i) == N(j) == N(P(i))$. Indeks predhodnika lahko pridobimo iz Bellmanove enačbe in sicer kjer je dosežen maksimum za $l(i)$. Torej potrebujemo postopek kako pridobiti indeks iz $max_{(j=0)and(N(j)<N(i))}^{i-1} l(j)$. Maksimum nam vrne maksimalno dolžino podzaporedij, ki se konča z $N(i)$. Preko indeksiranja v maksimumu bomo v $P(i)$ shranili indeks kjer je dosežen maksimum. Če takega indeksa ni potem je $P(i) == None$

#### Izpis zaporedja

V tem trenutku imamo zgenerirano celoten seznam $P$. Sedaj da zegeriramo nše zaporedje se držimo le formule:
$$[\dots,N(P(P(i))),N(P(i)),N(i)]$$
Na tak način zgeneriramo naše zaporedje, ki se konča z elementom N(i).

### Mnenje
Vaje so mi zelo všeč, saj skupaj analiziramo probleme. 

### Viri
Zapiski iz vaj.