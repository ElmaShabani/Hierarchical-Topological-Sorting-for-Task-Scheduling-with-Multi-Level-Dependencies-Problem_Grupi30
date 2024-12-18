class Graph:
    def __init__(self, num_nodes):
        """Inicializon një graf me numrin e nyjeve."""
        self.num_nodes = num_nodes
        self.adj_list = {i: [] for i in range(num_nodes)}

    def add_edge(self, u, v, weight=1):
        """Shton një lidhje me peshë në graf (u -> v)."""
        self.adj_list[u].append((v, weight))

    def display_graph(self):
        """Shfaq graf-in në formë tekstuale."""
        print("Grafi:")
        for node, neighbors in self.adj_list.items():
            print(f"{node} -> {[(n, w) for n, w in neighbors]}")

class DirectedAcyclicGraph(Graph):
    def __init__(self, num_nodes):
        """Inicializon një graf aciklik të drejtuar (DAG)."""
        super().__init__(num_nodes)
        self.visited = [False] * num_nodes
        self.rec_stack = [False] * num_nodes
        self.order = []
        self.cycles = []

    def detect_cycle(self, node, path):
        """DFS për të detektuar cikle dhe për të regjistruar nyjet e ciklit."""
        self.visited[node] = True
        self.rec_stack[node] = True
        path.append(node)

        for neighbor, _ in self.adj_list[node]:
            if not self.visited[neighbor]:
                if self.detect_cycle(neighbor, path):
                    return True
            elif self.rec_stack[neighbor]:
                cycle_start_index = path.index(neighbor)
                self.cycles.append(path[cycle_start_index:])
                return True

        self.rec_stack[node] = False
        path.pop()
        return False

    def topological_sort_util(self, node, priority):
        """Funksion ndihmës për renditjen topologjike duke përdorur DFS."""
        self.visited[node] = True

        # Rendor fqinjët bazuar në prioritetet
        neighbors = sorted(self.adj_list[node], key=lambda x: x[1], reverse=(priority == "high"))
        for neighbor, _ in neighbors:
            if not self.visited[neighbor]:
                self.topological_sort_util(neighbor, priority)

        self.order.append(node)

    def topological_sort(self, priority="low"):
        """Kryen renditjen topologjike dhe kontrollon për cikle."""
        self.visited = [False] * self.num_nodes
        self.order = []
        self.cycles = []

        # Kontrollo për cikle
        for node in range(self.num_nodes):
            if not self.visited[node]:
                if self.detect_cycle(node, []):
                    raise ValueError(f"Cikël i gjetur: {self.cycles}")

        # Kryej renditjen topologjike
        self.visited = [False] * self.num_nodes
        for node in range(self.num_nodes):
            if not self.visited[node]:
                self.topological_sort_util(node, priority)

        self.order.reverse()
        return self.order
            
def read_edges():
    """Funksioni per te lexuar detyrat dhe varesite nga tastiera ose nga file"""
    mode = input("Zgjidhni menyren e leximit (1 per tastiere, 2 per file): ").strip()
    edges = []
    num_tasks = 0

    if mode == "1":
        try:
            num_tasks = int(input("Numri i detyrave: "))
            num_edges = int(input("Numri i varesive: "))
            print("Shkruani varesite në formatin 'detyre1 detyre2', ku detyre1 varet nga detyre2:")
            for _ in range(num_edges):
                u, v = map(int, input("Varesia: ").split())
                edges.append((u, v))
        except ValueError:
            print("Input i pavlefshëm! Ju lutem shkruani numra të vlefshëm.")

    elif mode == "2":
        filename = input("Shkruani emrin e file-it: ").strip()
        try:
            with open(filename, 'r') as file:
                num_tasks = int(file.readline().strip())
                num_edges = int(file.readline().strip())
                for _ in range(num_edges):
                    u, v = map(int, file.readline().strip().split())
                    edges.append((u, v))
        except (ValueError, FileNotFoundError, IndexError) as e:
            print(f"Gabim gjatë leximit të file-it: {e}")

    else:
        print("Opsion i pavlefshëm.")

    return num_tasks, edges

# Funksioni kryesor për ekzekutimin e programit
if __name__ == "__main__":
    num_tasks, edges = read_edges()

    if num_tasks > 0 and edges:
        print("\nDetyrat dhe varësitë e lexuara:")
        print(f"Numri i detyrave: {num_tasks}")
        print(f"Varësitë: {edges}")

        # Krijoni graf-in dhe shtoni varësitë
        hts = HierarchicalTopologicalSort(num_tasks)
        for u, v in edges:
            hts.add_edge(u, v)

        # Kryeni renditjen topologjike
        try:
            result = hts.topological_sort()
            print("\nRenditja e vlefshme e detyrave:", result)
        except Exception as e:
            print("\nGabim:", e)
    else:
        print("Të dhënat e futura ishin të pavlefshme.")