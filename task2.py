import networkx as nx
import matplotlib.pyplot as plt

def create_graph():
    G = nx.Graph()
    cities = [
        "Київ", "Львів", "Одеса", "Харків", "Дніпро", "Запоріжжя", "Луцьк", 
        "Херсон", "Миколаїв", "Чернівці", "Івано-Франківськ", "Тернопіль", 
        "Рівне", "Житомир", "Вінниця", "Черкаси", "Полтава", "Суми", "Чернігів", 
        "Ужгород", "Кропивницький", "Маріуполь", "Краматорськ"
    ]

    roads = [
        ("Київ", "Львів"), ("Київ", "Одеса"), ("Київ", "Харків"), 
        ("Київ", "Дніпро"), ("Дніпро", "Запоріжжя"), ("Львів", "Луцьк"), 
        ("Луцьк", "Київ"), ("Одеса", "Дніпро"), ("Київ", "Чернігів"),
        ("Київ", "Житомир"), ("Житомир", "Львів"), ("Львів", "Івано-Франківськ"), 
        ("Івано-Франківськ", "Чернівці"), ("Тернопіль", "Чернівці"), 
        ("Тернопіль", "Львів"), ("Тернопіль", "Хмельницький"), 
        ("Хмельницький", "Вінниця"), ("Вінниця", "Київ"), ("Вінниця", "Ужгород"),
        ("Одеса", "Миколаїв"), ("Миколаїв", "Херсон"), ("Херсон", "Запоріжжя"), 
        ("Запоріжжя", "Маріуполь"), ("Маріуполь", "Краматорськ"), 
        ("Краматорськ", "Харків"), ("Харків", "Полтава"), ("Полтава", "Київ"), 
        ("Суми", "Полтава"), ("Суми", "Харків"), ("Суми", "Чернігів"), 
        ("Чернігів", "Полтава"), ("Ужгород", "Львів"), ("Кропивницький", "Дніпро"), 
        ("Кропивницький", "Миколаїв"), ("Кропивницький", "Київ"), 
        ("Черкаси", "Київ"), ("Черкаси", "Полтава"), ("Рівне", "Луцьк"), 
        ("Рівне", "Тернопіль")
    ]

    G.add_nodes_from(cities)
    G.add_edges_from(roads)
    return G

def run():
    G = create_graph()

    def dfs_path(graph, start, goal):
        stack = [(start, [start])]
        while stack:
            (vertex, path) = stack.pop()
            for next in set(graph.neighbors(vertex)) - set(path):
                if next == goal:
                    yield path + [next]
                else:
                    stack.append((next, path + [next]))

    def bfs_path(graph, start, goal):
        queue = [(start, [start])]
        while queue:
            (vertex, path) = queue.pop(0)
            for next in set(graph.neighbors(vertex)) - set(path):
                if next == goal:
                    yield path + [next]
                else:
                    queue.append((next, path + [next]))

    start_city = "Київ"
    goal_city = "Харків"

    dfs_paths = list(dfs_path(G, start_city, goal_city))
    bfs_paths = list(bfs_path(G, start_city, goal_city))

    def visualize_path(graph, path, title):
        pos = nx.spring_layout(graph)
        plt.figure(figsize=(12, 8))
        nx.draw(graph, pos, with_labels=True, node_size=700, node_color="lightblue", font_size=10, font_weight="bold")
        path_edges = list(zip(path, path[1:]))
        nx.draw_networkx_edges(graph, pos, edgelist=path_edges, edge_color='r', width=2)
        nx.draw_networkx_nodes(graph, pos, nodelist=path, node_color='r')
        plt.title(title)
        plt.show()

    dfs_first_path = dfs_paths[0]
    visualize_path(G, dfs_first_path, "DFS Path from Kyiv to Kharkiv")

    bfs_first_path = bfs_paths[0]
    visualize_path(G, bfs_first_path, "BFS Path from Kyiv to Kharkiv")

    print("DFS Paths:")
    for path in dfs_paths:
        print(" -> ".join(path))

    print("\nBFS Paths:")
    for path in bfs_paths:
        print(" -> ".join(path))

if __name__ == "__main__":
    run()
