from big_graph.int_directed_big_graph import IntDirectedBigGraph
from big_graph.string_undirected_big_graph import StringUnDirectedBigGraph


def test_directed_graph():
    directed_big_graph = IntDirectedBigGraph()
    directed_big_graph.generate_data(1000, 5000)

    directed_big_graph.save_graph('./data/directed_random_graph.txt')

    directed_big_graph.load_graph('./data/directed_random_graph.txt')

    print(directed_big_graph.in_neighbors(5))
    print(directed_big_graph.out_neighbors(5))
    print(directed_big_graph.is_edge(5, 2))
    directed_big_graph.add_node(-1)
    print(directed_big_graph.get_node(-1))
    directed_big_graph.add_edge(-1, 1)
    directed_big_graph.add_edge(1, -1)
    print(directed_big_graph.get_node(-1))

    path = directed_big_graph.dfs(5)
    with open('./data/directed_edges_traversed.txt', 'w') as file:
        number_node_in_path = len(path)
        for idx, node in enumerate(path):
            if idx + 1 < number_node_in_path:
                next_node = path[idx + 1]
                edge_str = f'{node}, {next_node}'
                file.write(f'( {edge_str} )' + '\n')

    print("done")


def test_undirected_graph():
    undirected_graph = StringUnDirectedBigGraph()
    undirected_graph.generate_data(10000, 90000)
    undirected_graph.save_graph('./data/undirected_random_graph.txt')

    undirected_graph.load_graph('./data/undirected_random_graph.txt')

    undirected_graph.add_node("what")
    print(undirected_graph.get_node("what"))
    undirected_graph.add_edge("what", "somehow")
    print(undirected_graph.is_edge("what", "somehow"))
    print(undirected_graph.get_node("what"))

    path = undirected_graph.dfs("what")
    with open('./data/undirected_edges_traversed.txt', 'w') as file:
        number_node_in_path = len(path)
        for idx, node in enumerate(path):
            if idx + 1 < number_node_in_path:
                next_node = path[idx + 1]
                edge_str = f'{node}, {next_node}'
                file.write(f'( {edge_str} )' + '\n')

    print("done")


if __name__ == '__main__':
    test_undirected_graph()
    # test_directed_graph()
