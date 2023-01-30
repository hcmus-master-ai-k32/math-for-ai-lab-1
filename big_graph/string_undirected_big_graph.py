from .base_undirected_big_graph import BaseUnDirectedBigGraph


# TODO
class StringUnDirectedBigGraph(BaseUnDirectedBigGraph):
    def generate_data(self, num_nodes, num_edges):
        """Generate data for a graph with a given number of nodes and edges"""
        pass

    def load_graph(self, file_path):
        """
        Load a graph from a file
        Format file: node, then the rest is neighbor nodes
        """
        pass
