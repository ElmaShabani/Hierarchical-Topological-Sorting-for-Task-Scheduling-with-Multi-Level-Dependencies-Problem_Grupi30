class HierarchicalTopologicalSort:
    def __init__(self, num_tasks):
        """Inicializon graf-in me numrin e nyjeve (detyrave)"""
        self.num_tasks = num_tasks
        self.adj = [[] for _ in range(num_tasks)]  # Lista e fqinjeve per graf-in
        self.visited = [False] * num_tasks  # Vizituar per ruajtjen e vizitave te nyjeve
        self.stack = []  # Staku per ruajtjen e renditjes topologjike