class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        # Add an item to the end of the queue
        self.items.append(item)

    def dequeue(self):
        # Remove and return the first item from the queue
        if not self.is_empty():
            return self.items.pop(0)

    def is_empty(self):
        # Check if the queue is empty
        return len(self.items) == 0

class Graph:
    def __init__(self):
        # Initialize an empty graph represented by a dictionary
        self.graph = {}

    def add_edge(self, node, adjacent):
        # Add an edge between nodes in the graph
        if node not in self.graph:
            self.graph[node] = []
        self.graph[node].append(adjacent)

    def bfs(self, start_node):
        # Perform Breadth-First Search traversal starting from the given start node
        visited = set()  # Keep track of visited nodes
        queue = Queue()   # Initialize a queue for BFS traversal
        queue.enqueue(start_node)  # Enqueue the start node
        visited.add(start_node)    # Mark the start node as visited

        while not queue.is_empty():
            # Dequeue a node from the queue
            current_node = queue.dequeue()
            print(current_node, end=" ")  # Print the current node

            if current_node in self.graph:
                # Traverse the adjacent nodes of the current node
                for adjacent in self.graph[current_node]:
                    if adjacent not in visited:
                        # Enqueue adjacent nodes if not visited and mark them as visited
                        queue.enqueue(adjacent)
                        visited.add(adjacent)

# Example Usage:
g = Graph()
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(2, 4)
g.add_edge(2, 5)
g.add_edge(3, 6)
g.add_edge(3, 7)

print("BFS Traversal:")
g.bfs(1)
