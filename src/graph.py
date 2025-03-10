import networkx as nx


def create_graph(edges: list[tuple[int, int]]) -> nx.Graph:
    """
    Membuat graf tidak berarah berdasarkan daftar sisi yang diberikan.

    Parameters:
    edges (list[tuple[int, int]]): Daftar sisi yang menghubungkan dua simpul.

    Returns:
    nx.Graph: Objek graf dari NetworkX.
    """
    graph = nx.Graph()  # Membuat objek graf kosong
    graph.add_edges_from(edges)  # Menambahkan semua sisi ke graf
    return graph


def get_degree(G: nx.Graph, node: int) -> int:
    """
    Menghitung derajat dari simpul tertentu dalam graf.

    Parameters:
    G (nx.Graph): Graf yang telah dibuat.
    node (int): Simpul yang ingin dihitung derajatnya.

    Returns:
    int: Derajat dari simpul tersebut.
    """
    return G.degree(node)


def dfs_traversal(G: nx.Graph, start: int) -> list[int]:
    """
    Melakukan pencarian Depth-First Search (DFS) mulai dari simpul tertentu.

    Parameters:
    G (nx.Graph): Graf yang telah dibuat
    start (int): Simpul awal traversal

    Returns:
    list[int]: Urutan kunjungan simpul sesuai DFS
    """
    return list(nx.dfs_preorder_nodes(G, source=start))


def bfs_traversal(G: nx.Graph, start: int) -> list[int]:
    """
    Melakukan pencarian Breadth-First Search (BFS) mulai dari simpul tertentu.

    Parameters:
    G (nx.Graph): Graf yang telah dibuat
    start (int): Simpul awal traversal

    Returns:
    list[int]: Urutan kunjungan simpul sesuai BFS
    """
    return [start] + [v for u, v in nx.bfs_edges(G, start)]


def find_shortest_path(G: nx.Graph, source: int, target: int) -> list[int]:
    """
    Mencari jalur terpendek antara dua simpul dalam graf tidak berarah.

    Parameters:
    G (nx.Graph): Graf yang telah dibuat
    source (int): Simpul awal
    target (int): Simpul tujuan

    Returns:
    list[int]: Urutan simpul dalam jalur terpendek
    """
    try:
        return nx.shortest_path(G, source=source, target=target)
    except:
        return None


import matplotlib.pyplot as plt


def visualize_graph(G: nx.Graph) -> None:
    """
    Memvisualisasikan graf menggunakan matplotlib dan menyimpan sebagai PNG.

    Parameters:
    G (nx.Graph): Graf yang akan divisualisasikan

    Output:
    None (menghasilkan file PNG dan menampilkan visualisasi)
    """
    plt.figure(figsize=(10, 8))

    # Menggunakan layout spring untuk tata letak node
    pos = nx.spring_layout(G, seed=42)  # seed untuk konsistensi visual

    # Menggambar graf dengan styling
    nx.draw(
        G,
        pos,
        with_labels=True,
        node_color="skyblue",
        edge_color="grey",
        node_size=800,
        font_size=12,
        font_weight="bold",
        width=1.5,
    )

    # Menyimpan gambar ke file
    plt.savefig(
        "graph_visualization.png", dpi=300, bbox_inches="tight", facecolor="white"
    )

    # Menampilkan visualisasi
    plt.show()
    plt.close()  # Menutup plot untuk menghindari memory leak
