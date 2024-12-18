import networkx as nx
import matplotlib.pyplot as plt 

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

    def visualize_graph(self):
        """Vizualizon graf-in duke përdorur NetworkX dhe Matplotlib."""
        G = nx.DiGraph()  # Graf i orientuar (Directed Graph)
        
        # Shto nyjet dhe lidhjet
        for node, neighbors in self.adj_list.items():
            for neighbor, weight in neighbors:
                G.add_edge(node, neighbor, weight=weight)
        
        # Vizualizimi
        pos = nx.spring_layout(G)  # Layout i nyjeve
        labels = nx.get_edge_attributes(G, 'weight')  # Etiketat e peshës
        
        nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=2000, font_size=10, font_weight='bold')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)  # Vendos peshat e lidhjeve
        
        plt.title("Vizualizimi i Grafit")
        plt.show()

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
   
   
def read_data():
    """Lexon të dhënat nga tastiera ose file."""
    mode = input("Zgjidhni mënyrën e leximit (1 për tastierë, 2 për file): ").strip()
    dependencies = []
    num_tasks = 0

    if mode == "1":
        try:
            num_tasks = int(input("Numri i detyrave: "))
            num_dependencies = int(input("Numri i varësive: "))
            print("Shkruani varësitë në formatin 'detyre1 detyre2 peshë' (peshë është opsionale):")

            for _ in range(num_dependencies):
                inputs = input("Varësia: ").split()
                u, v = int(inputs[0]), int(inputs[1])
                weight = int(inputs[2]) if len(inputs) > 2 else 1
                dependencies.append((u, v, weight))
        except ValueError:
            print("Input i pavlefshëm!")
    elif mode == "2":
        filename = input("Shkruani emrin e file-it: ").strip()
        try:
            with open(filename, 'r') as file:
                num_tasks = int(file.readline().strip())
                num_dependencies = int(file.readline().strip())
                for _ in range(num_dependencies):
                    inputs = file.readline().strip().split()
                    u, v = int(inputs[0]), int(inputs[1])
                    weight = int(inputs[2]) if len(inputs) > 2 else 1
                    dependencies.append((u, v, weight))
        except (ValueError, FileNotFoundError, IndexError) as e:
            print(f"Gabim gjatë leximit të file-it: {e}")
        else:
            print("Opsion i pavlefshëm. Ju lutem zgjidhni 1 ose 2.")

    return num_tasks, dependencies

if __name__ == "__main__":
    num_tasks, dependencies = read_data()

    dag = DirectedAcyclicGraph(num_tasks)
    for u, v, weight in dependencies:
        dag.add_edge(u, v, weight)

    dag.display_graph()

    print("\nVizualizimi i grafit:")
    dag.visualize_graph()  # Vizualizo graf-in

    try:
        print("\nRenditja topologjike me prioritet të ulët (low):")
        result_low = dag.topological_sort(priority="low")
        print(result_low)

        print("\nRenditja topologjike me prioritet të lartë (high):")
        result_high = dag.topological_sort(priority="high")
        print(result_high)
    except ValueError as e:
        print("Gabim:", e)
