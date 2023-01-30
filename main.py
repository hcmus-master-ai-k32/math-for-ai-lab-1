from big_graph.int_directed_big_graph import IntDirectedBigGraph


if __name__ == '__main__':
    directed_big_graph = IntDirectedBigGraph()
    directed_big_graph.generate_data(1000, 5000)

    directed_big_graph.save_graph('./data/random_graph.txt')

    directed_big_graph.save_graph('./data/saved_graph.txt')

    directed_big_graph.load_graph('./data/random_graph.txt')

    print(directed_big_graph.in_neighbors(5))
    print(directed_big_graph.out_neighbors(5))
    print(directed_big_graph.is_edge(5, 2))
    directed_big_graph.add_node(-1)
    print(directed_big_graph.get_node(-1))
    directed_big_graph.add_edge(-1, 1)
    directed_big_graph.add_edge(1, -1)
    print(directed_big_graph.get_node(-1))

    edges_traversed = directed_big_graph.dfs(5)
    with open('./data/edges_traversed.txt', 'w') as file:
        for edge in edges_traversed:
            edge_str = ', '.join(map(str, edge))
            file.write(f'( {edge_str} )' + '\n')
