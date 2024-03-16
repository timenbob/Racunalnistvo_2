## Poročilo za Računalništvo 2 - 0/1 Nahrbtnik
* Avtor : Timen Bobnar 
* Datum : 16.3.2024

### Povzetek

Na prvih vajah smo ponovili kaj je O-notacija. Ogledali smo si tudi kje se uporablja različne programerske strukture glede na njihove časovne omejitve pri dodajanju, brisanju, ... podatkov. Analizirali smo problem deljenja palice, zanj ispeljali Bellmanovo enačbo in opravili časovno analizo. 
Na drugih vajah smo ponovili kaj je 0/1 nahrbtnik ter izpeljali Bellmanovo enačno, opravili časovno analizo in pokazali 4 različne probleme glede na to ali lahko element režemo in ali nastopajo kopije. Sprogramirali smo nekaj rešitev na Tomo-tu. Povedali smo tudi kako se poleg optimalne vrednosti izračuna tudi optimalno rešitev.
Na tretjih vajah smo si ogledali nekaj rešitev iz vaje 2. Povedali smo kaj je požrešna metoda in naredili 2 implementaciji na 0/1-nahrbtnik. Iskali smo tudi primer kjer se pojavi največja razlika med osnovnim algoritmom in požrešno metodo.
Na četrtih vajah smo si ogledali par različnih implementacij 0/1 Nahrbtnika. Ponovno smo implementirali nalogo kjer se lahko elementi ponavljajo vendar, da smo tokrat razvili novo Bellmanovo enačbo. Ogledali smo si še problema kjer imamo nekaj števil in nas zanima ali lahko s temi števili sestavimo neko drugo število. Tu smo imeli 2 primera. Prvi primer ima omejeno koliko števil lahko izberemo drugi pa ne. Za oba primera smo izpeljali Bellmanovo enačbo.

### Opis problema
V tem problemu bomo obravnavali eno od verzij 0/1 Nahrbtnika in sicer tisto kjer se lahko predmeti pojavijo veckrat. 
Vhodni podatki so volumen nahrbtnika (W) ter seznam različnih predmetov(A), za vsak predmet imamo podan volumen in ceno(v,c).
Vsak element iz seznama A lahko nastopi večkrat. Zanima nas maksimalna vrednost našega nahrbtnika.
Kor izhodni podatek bi radi podali število, ki je enako vrednosti oprimalnega nahrbtnika.
```
W=30
A=[(10,6),(15,3),(20,12)]
Da dobimo optimalno vrednost, ki je 18 lahko izberemo 3x(10,6). To je sprejemljiva rešitev, saj se predmeti lahko ponavljajo. 
```
Naš problem lahko rešimo na 2 načina.

#### Prvi način
V prvem načinu naše osnovne podatke spremenimo. Volumen nahrbtnika ostane isti vendam seznam elementov bomo povečali.

##### Rešitev
Za vsak element v seznamu A pogledamo kolikokrat ga lahko vstavimo v naš nahrbtnik, nato naš element tolikokrat ponovimo.
```
W=30
A=[(10,6),(15,3),(20,12)]
Pogljemo kolikokrat lahko element (10,6) vstavimo v naš nahrbnik. Opazimo da 3krat, saj 4krat bi že presegli volumen nahrbnika.
Pogljemo kolikokrat lahko element (15,3) vstavimo v naš nahrbnik. Opazimo da 2krat.
Pogljemo kolikokrat lahko element (20,12) vstavimo v naš nahrbnik. Opazimo da 1krat.
Naš novi seznam A je torej [(10,6),(10,6),(10,6),(15,3),(15,3),(20,12)]
```
Na naših novih podatkih sedaj izvedemo navadno Bellmanovo enačbo za 0/1-Nahrbtnik.
```
G(i,W)=max{c_i + G(i-1,W-v_i),G(i-1,W)}
```
V formuli i predtsvlja i-ti predmeti c_i vrednost oziroma ceno itega predmeta ter v_i volumen itega predmeta.

##### Slabosti
Ta pristo je slab, saj se nam lahko zgodi, da se nam elemeti velikokrat podvojijo na primer vsak element dobi 1000 kopij to bi bilo zelo slabo zaradi časa, ki bi ga potrebovali da rešimo problem. Časovna analiza nam vrne O(n*W) in v primeru, da se vsak n ponovi velikokrat lahko opazimo, da problem eksplodira.

#### Drugi način
V drugem načinu ustavrimo novo Bellmanovo enačbo.

```
G(W)=max{G(W-v_i)+c_i}; kjer max teče od i=1 do n.
```
V tej formuli na vsakem koraku preverimo kateri od n elementov se nam najbolj splača dodati (pregledamo vse elemente vsakič).
Ko ugotovimo kateri je ta element našemu volumno odštejemo volumen tega elementa in vrednst elementa prištejemo prištejemo. Na koncu vrnemo optimalno vrednost nahrbtnika. 

##### Časovna analiza
V tej formuli dobimo, da je časovna analiza O(n*W), kjer n predstavlja število elementov.

### Podobni problem
Razporejanje opravil: Imamo seznam opravil s časovnimi in vrednostnimi vrednostmi. Cilj je izbrati največje število opravil, ki jih lahko izvedemo v določenem časovnem okviru, tako da je skupna vrednost maksimalna.

### Mnenje
Vaje so mi zelo všeč, saj skupaj analiziramo probleme. 

### Viri
Zapiski iz vaj.