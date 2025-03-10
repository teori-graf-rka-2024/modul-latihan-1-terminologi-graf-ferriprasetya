# tutorial.py
from graph import (
    create_graph,
    get_degree,
    dfs_traversal,
    bfs_traversal,
    find_shortest_path,
    visualize_graph,
)

# Contoh daftar sisi (edges)
edges = [(1, 2), (2, 3), (3, 4), (4, 1), (2, 5), (5, 6), (3, 6), (4, 7)]

# 1. Membuat graf
print("1. Membuat graf dari edges...")
G = create_graph(edges)
print(f"Jumlah node: {len(G.nodes)}")
print(f"Jumlah edge: {len(G.edges)}\n")

# 2. Menghitung derajat node
print("2. Menghitung derajat node:")
nodes_to_check = [2, 5, 7]
for node in nodes_to_check:
    print(f"Derajat node {node}: {get_degree(G, node)}")
print()

# 3. DFS Traversal
print("3. DFS Traversal mulai dari node 1:")
dfs_result = dfs_traversal(G, 1)
print(f"Hasil DFS: {dfs_result}\n")

# 4. BFS Traversal
print("4. BFS Traversal mulai dari node 1:")
bfs_result = bfs_traversal(G, 1)
print(f"Hasil BFS: {bfs_result}\n")

# 5. Mencari jalur terpendek
print("5. Mencari jalur terpendek:")
paths_to_find = [(1, 6), (3, 7), (1, 8)]  # 8 adalah node tidak ada
for source, target in paths_to_find:
    path = find_shortest_path(G, source, target)
    if path:
        print(f"Jalur dari {source} ke {target}: {path}")
    else:
        print(f"Tidak ada jalur dari {source} ke {target}")
print()

# 6. Visualisasi graf
print("6. Memvisualisasikan graf...")
visualize_graph(G)
print("Visualisasi telah disimpan sebagai graph_visualization.png")
