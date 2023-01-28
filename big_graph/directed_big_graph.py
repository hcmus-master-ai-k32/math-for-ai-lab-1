import bisect
import random


class DirectedBigGraph:
    """
    This graph current only support int data type
    """

    def __init__(self):
        # Key is node
        # Value is a tuple with 2 arrays
        # - First array is in-neighbors of node
        # - Second array is out-neighbors of node
        self.graph = {}

    def in_neighbors(self, node):
        """Return the in-neighbors of a node"""
        return self.graph[node][0]

    def out_neighbors(self, node):
        """Return the out-neighbors of a node"""
        return self.graph[node][1]

    def generate_data(self, num_nodes, num_edges):
        """Generate data for a graph with a given number of nodes and edges"""
        nodes = [i for i in range(num_nodes)]
        for node in nodes:
            self.graph[node] = ([], [])  # initialize in-neighbors and out-neighbors for each node

        edges = 0
        while edges < num_edges:
            node1 = random.choice(nodes)
            node2 = random.choice(nodes)

            if node1 == node2:
                continue  # ignore self-loops
            if node2 in self.graph[node1][1]:
                continue
            self.graph[node1][1].append(node2)

            edges += 1

    def load_graph(self, file_path):
        """
        Load a graph from a file
        Format file: node, then the rest is out-neighbor nodes
        """
        self.graph = {}
        with open(file_path, 'r') as file:
            for line in file:
                line = line.strip().split()
                node = int(line[0])
                if node not in self.graph:
                    self.graph[node] = [[], []]
                for neighbor in line[1:]:
                    neighbor = int(neighbor)

                    self.graph[node][1].append(neighbor)
                    if neighbor not in self.graph:
                        self.graph[neighbor] = [[], []]
                    self.graph[neighbor][0].append(node)

        for node in self.graph:
            self.graph[node][0].sort()
            self.graph[node][1].sort()

    def save_graph(self, file_path):
        """Save a graph to a file"""
        with open(file_path, 'w') as file:
            for node in self.graph:
                file.write(str(node) + ' ' + ' '.join(map(str, self.graph[node][1])) + '\n')

    def add_node(self, node):
        """Add a node to the graph"""
        if node not in self.graph:
            self.graph[node] = ([], [])

    def get_node(self, node):
        """Return the in-neighbors and out-neighbors of a given node"""
        if node in self.graph:
            return self.graph[node]
        else:
            raise ValueError(f"{node} is not in the graph")

    def remove_node(self, node):
        """Remove a node and all its edges from the graph"""
        if node not in self.graph:
            print(f'Error: node {node} not in the graph')
            return
        # remove all edges from the node
        for neighbor in self.graph[node][1]:
            index = bisect.bisect_left(self.graph[neighbor][0], node)
            del self.graph[neighbor][0][index]
        for neighbor in self.graph[node][0]:
            index = bisect.bisect_left(self.graph[neighbor][1], node)
            del self.graph[neighbor][1][index]
        # remove the node from the graph
        del self.graph[node]

    def add_edge(self, node1, node2):
        """Add an directed edge from node1 to node2"""
        self.add_node(node1)
        self.add_node(node2)
        bisect.insort(self.graph[node1][1], node2)
        bisect.insort(self.graph[node2][0], node1)

    def is_edge(self, node1, node2):
        """Check if an edge exists between two nodes"""
        if node1 in self.graph and node2 in self.graph:
            if node2 in self.graph[node1][1]:
                return True
            else:
                return False
        else:
            raise ValueError(f"Either {node1} or {node2} is not in the graph")

    def remove_edge(self, node1, node2):
        """Remove an edge from the graph"""
        if node1 not in self.graph:
            print(f'Error: node {node1} not in the graph')
            return

        if node2 not in self.graph:
            print(f'Error: node {node2} not in the graph')
            return

        index = bisect.bisect_left(self.graph[node1][1], node2)
        del self.graph[node1][1][index]
        index = bisect.bisect_left(self.graph[node2][0], node1)
        del self.graph[node2][0][index]

    def dfs(self, start_node):
        if start_node not in self.graph:
            raise ValueError(f"{start_node} not exists in graph")

        visited = set()
        stack = [(start_node, None)]
        edges = []

        while stack:
            node, prev_edge = stack.pop()
            if node not in visited:
                visited.add(node)

                for neighbor in self.out_neighbors(node):
                    stack.append((neighbor, node))
                    if (node, neighbor) not in edges:
                        edges.append((node, neighbor))

        return edges
