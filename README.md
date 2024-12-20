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
