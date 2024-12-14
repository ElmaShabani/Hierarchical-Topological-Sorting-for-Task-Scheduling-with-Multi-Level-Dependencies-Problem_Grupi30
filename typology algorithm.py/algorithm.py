class HierarchicalTopologicalSort:
    def __init__(self, num_tasks):
        """Inicializon graf-in me numrin e nyjeve (detyrave)"""
        self.num_tasks = num_tasks
        self.adj = [[] for _ in range(num_tasks)]  # Lista e fqinjeve per graf-in
        self.visited = [False] * num_tasks  # Vizituar per ruajtjen e vizitave te nyjeve
        self.stack = []  # Staku per ruajtjen e renditjes topologjike

    def add_edge(self, u, v):
        """Shton nje lidhje ne graf (u -> v)"""
        self.adj[u].append(v)

    def topological_sort_util(self, v):
        """Funksioni ndihmes per te realizuar topological sort (DFS)"""
        # Marko nyjen si të vizituar
        self.visited[v] = True

        #  DFS per nyjet fqinje
        for neighbor in self.adj[v]:
            if not self.visited[neighbor]:
                self.topological_sort_util(neighbor)

        self.stack.append(v)
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