## Poročilo za Računalništvo 2 - Računanje najkrajših poti v grafu
* Avtor : Timen Bobnar 
* Datum : 11.5.2024

### Povzetek

V tem poročilu primerjamo vse različne algoritme za računanje njkrajših poti v grafu.
Algoritimi:
* Floyd-Warshall algoritem
* Djikstrov algoritem
* Iskanje najkrajših (in najdaljših) poti v DAG-ih (usmerjenih grafih brez ciklov)
* Bellman-Ford algoritem

### Floyd-Warshall algoritem
#### Uporaba: 
F-W algoritem se uporablja ko iščemo najkrajše poti med vsemi pari vozlišč.\
Primer: Imamo 10 prijateljev vsak živi v na drugačnem naslovu(vozlišču), vseh 10 prijateljev bi se radi dobili na trgu mesta(enajsto vozlišče). Izračunajte za vsakega prijatelja kakšna je dolžina njegove pote do trga. Dolžina poti je odvisna od dolžine ceste.

#### Prednosti:
* Enostavna implementacija.
* Naenkrat dobimo vse najkrajše poti.
* Deluje tudi za grafe z negativnimi utežmi.

#### Slabosti:
* Časovna zahtevnst je $O(n^3)$, kjer je $n$ število vozlišč.
* Prostorska zahtevnst je $O(n^2)$, kjer je $n$ število vozlišč.

#### Priporočilo
Ta algoritem je primeren za manjše grafe, saj ima veliko časovno zahtevnost. Uporabimo ga ko želimo vse najkrajše poti in imamo povezave v grafu negativne.

### Dijkstrov algoritem
#### Uporaba: 
Dijkstra algoritem se uporablja za iskanje najkrajših poti od enega vozlišča(izvora), do vseh ostalik\
Primer: Navigacijski sistemi. 

#### Prednosti:
* Učinkovit za grafe z nenegativnimi utežmi.
* Potrebuje manj prostora kot Floyd-Warshall algoritem.
* Časovna zahtevnost: $O((n + e) * log n)$, kjer je $n$ število vozlišč in $e$ število povezav v grafu.

#### Slabosti:
* Ne deluje pravilno za grafe z negativnimi utežmi.
* Prostorska zahtevnost: $O(n + e)$,kjer je $n$ število vozlišč in $e$ število povezav v grafu.

#### Priporočilo
Ta algoritme je primeren za grafe, ki imajo veliko vozlišč in povezav kjer povezave niso negativne in iščemo najkrajšo pot od enega vozlišča do vseh ostalih.

### Iskanje najkrajših (in najdaljših) poti v DAG-ih (usmerjenih grafih brez ciklov)
#### Uporaba: 
Primeren je za iskanje najkrajših (ali najdaljših) poti v usmerjenih acikličnih grafih (DAG).\
Primer: Kjer koli kjer lahko graf predstavimo kot usmerjeni graf brez ciklov

#### Prednosti:
* Časovna zahtevnost: $O(n + e)$, kjer je $n$ število vozlišč in $e$ število povezav v grafu.
* Prostorska zahtevnost: $O(n)$, kjer je $n$ število vozlišč.

#### Slabosti:
* Ne deluje pravilno za grafe z negativnimi utežmi.

#### Priporočilo
Ta algoritem lahko uporaimo na usmerjenih acikličnih grafih, kjer so uteži pozitivne. Algoritem nam za tak graf vrne najkrajšo oziroma najdaljšo poto.

### Bellman-Ford algoritem
#### Uporaba: 
Uporablja se ga ko imamo negativne uteži na grafu\
Primer: Iskanje arbitraža pri spreminjanju valut denarja.

#### Prednosti:
* Deluje za grafe z negativnimi utežmi in lahko zazna negativne cikle.
* Prostorska zahtevnost: $O(n)$, kjer je $n$ število vozlišč.

#### Slabosti:
* Časovna zahtevnost: $O(n * e)$, kjer je $n$ število vozlišč in $e$ število povezav v grafu.

#### Priporočilo
Ta algoritme se uporablja za redke grafe z negativnimu utežmi.

### Priporočila glede na tip grafa
* Redek graf z negativnimi utežmi: Uporabite Bellman-Ford algoritem, saj učinkovito obravnava negativne uteži in zaznava negativne cikle.
* Gost graf z nenegativnimi utežmi: Uporabite Dijkstra algoritem za iskanje najkrajših poti od enega vozlišča do vseh ostalih.
* Graf z negativnimi utežmi in potrebujete vse najkrajše poti: Uporabite Floyd-Warshall algoritem, čeprav je počasnejši, je primeren za manjše grafe.
* Usmerjeni aciklični graf (DAG): Uporabite algoritem za iskanje najkrajših poti v DAG-ih, ki je zelo učinkovit za tovrstne strukture.

### Mnenje
Vaje so mi bile všeč in zanimive.

### Viri
* Zapiski iz vaj.
* ChatGPT