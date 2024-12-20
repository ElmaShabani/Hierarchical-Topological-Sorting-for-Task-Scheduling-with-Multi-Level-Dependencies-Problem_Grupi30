# Hierarchical-Topological-Sorting-for-Task-Scheduling-with-Multi-Level-Dependencies
Ky projekt implementon funksionalitete për të punuar me grafë të orientuar dhe pa cikle

 # Funksionalitetet
- Krijimin dhe menaxhimin e një strukture grafi.
- Shtimin e lidhjeve të drejtuara me ose pa peshë opsionale.
- Vizualizimin e grafit duke përdorur NetworkX dhe Matplotlib.
- Zbulimin e cikleve brenda grafit.
- Kryerjen e renditjes topologjike me prioritet të personalizueshëm (i lartë/i ulët).
- Leximin e të dhënave nga input-i i përdoruesit ose nga një skedar.
----
# Kerkesat
- Sigurohuni që keni të instaluar:
- **Python 3.7 ose më i ri**
- ***Bibliotekat**: 
  - `NetworkX`
  - `Matplotlib`

Për të instaluar këto biblioteka, përdorni komandën:

**`pip install networkx matplotlib`**


## Karakteristikat

### Klasa `Graph`

- **`add_edge(u, v, weight=1)`**: Shton një lidhje të drejtuar nga nyja `u` te nyja `v` me një peshë opsionale.
- **`display_graph()`**: Shfaq graf-in në formë liste fqinjësie.
- **`visualize_graph()`**: Vizualizon graf-in duke përdorur `NetworkX` dhe `Matplotlib`.

### Klasa `DirectedAcyclicGraph`

Trashëgon nga klasa `Graph` dhe shton veçori specifike për DAG:

- **Detektimi i Cikleve**: Zbulon dhe tregon nëse ekziston një cikël në graf.
- **Renditja Topologjike**: Ofron renditjen e nyjeve bazuar në varësitë me dy mënyra prioritare:
  - `low`: Lidhjet me peshë më të ulët kanë përparësi.
  - `high`: Lidhjet me peshë më të lartë kanë përparësi.

------------------------------------------------------
## Ekzekutimi i Skriptit:

 Ruani kodin në një file me emrin dag.py dhe ekzekutojeni duke përdorur Python:

 python dag.py


##### Mënyrat e Futjes së Të Dhënave:

Mënyra 1: Jepni të dhënat direkt nga tastiera.

Specifikoni numrin e nyjeve dhe lidhjeve.
Futni lidhjet në formatin: nyje1 nyje2 pesha.
Mënyra 2: Ngarkoni të dhënat nga një file.


File duhet të ketë formatin:
numri_total_nyjeve 
numri_total_lidhjeve
nyje1 nyje2 pesha
Shembull Futjesh:


1. Nga tastiera:

Numri i detyrave: 4 <br>
Numri i varësive: 3 <br>
Varësia: 0 1 5 <br>
Varësia: 1 2 2 <br>
Varësia: 2 3 1 <br>


2. Nga file: File input.txt:

4 <br>
3 <br>
0 1 5 <br>
1 2 2 <br>
2 3 1 <br>
Rezultatet e Pritshme:
1. Vizualizimi i grafit.
2. Renditja topologjike me prioritet të lartë dhe të ulët.
3. Njoftim për cikle në rast se ekzistojnë.

   
### Struktura e Kodit
##### Klasa Graph:
Menaxhon grafet e drejtuara.
Shton lidhje dhe vizualizon grafet.

#####  Klasa DirectedAcyclicGraph:
Trashëgon nga Graph.
Implementon funksione për zbulimin e cikleve dhe renditjen topologjike.

##### Funksioni read_data:
Lexon të dhënat nga tastiera ose file.

##### Funksioni main:
Kontrollon rrjedhën e programit dhe ekzekuton funksionet kryesore.

Shembull Output-i <br>
Për të dhënat: <br>
Numri i detyrave: 4 <br>
Numri i varësive: 3 <br>
Varësia: 0 1 5 <br>
Varësia: 1 2 2 <br>
Varësia: 2 3 1 <br>

Output-i i pritshëm: <br>
Grafi: <br>
0 -> [(1, 5)] <br>
1 -> [(2, 2)] <br>
2 -> [(3, 1)] <br>
3 -> [] <br>

Vizualizimi i grafit: <br>
![image](https://github.com/user-attachments/assets/bc93bc5f-33ed-46ea-a9f0-5a8ef3e2aea7)


Renditja topologjike me prioritet të ulët (low): <br>
[0, 1, 2, 3] <br>

Renditja topologjike me prioritet të lartë (high): <br>
[0, 1, 2, 3] <br>


Gabimet e Mundshme <br>
Cikle në graf: Programi do të ndalojë dhe do të raportojë ciklin. <br>
Input i gabuar: Kontrolloni formatin e të dhënave dhe sigurohuni që janë të sakta. <br>

Kontributi <br>
Kontribues: <br>
[Armenie Sadikaj](https://github.com/armeniasadikaj) <br>
[Besarta Mustafa](https://github.com/BesartaMustafa1) <br>
[Elma Shabani](https://github.com/ElmaShabani) <br>
[Elisa Berisha](https://github.com/ElisaBerisha) <br>
Ndryshime dhe përmirësime janë të mirëpritura!


