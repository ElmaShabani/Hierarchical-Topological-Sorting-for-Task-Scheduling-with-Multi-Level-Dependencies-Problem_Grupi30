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

        def topological_sort(self):
        """Funksioni kryesor per te kryer topological sort dhe detektimin e cikleve"""
        #  DFS per nyje te pa vizituar ende
        for i in range(self.num_tasks):
            if not self.visited[i]:
                self.topological_sort_util(i)

        # renditja topologjike
        result = []
        while self.stack:
            result.append(self.stack.pop())
        return result