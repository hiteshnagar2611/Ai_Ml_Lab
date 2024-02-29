class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, node, adjacent):
        # Add an edge between nodes in the graph
        if node not in self.graph:
            self.graph[node] = []
        self.graph[node].append(adjacent)

    def dfs_util(self, node, visited):
        # Recursive utility function for DFS traversal
        visited.add(node)
        print(node, end=" ")

        if node in self.graph:
            for adjacent in self.graph[node]:
                if adjacent not in visited:
                    self.dfs_util(adjacent, visited)

    def dfs(self, start_node):
        # Perform Depth-First Search traversal starting from the given start node
        visited = set()  # Keep track of visited nodes
        self.dfs_util(start_node, visited)

# Example Usage:
g = Graph()
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(2, 4)
g.add_edge(2, 5)
g.add_edge(3, 6)
g.add_edge(3, 7)

print("DFS Traversal:")
g.dfs(1)
