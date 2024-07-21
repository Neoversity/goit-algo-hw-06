import networkx as nx
import matplotlib.pyplot as plt
import random
import heapq


def create_graph():
    G = nx.Graph()
    cities = [
        "Київ",
        "Львів",
        "Одеса",
        "Харків",
        "Дніпро",
        "Запоріжжя",
        "Луцьк",
        "Херсон",
        "Миколаїв",
        "Чернівці",
        "Івано-Франківськ",
        "Тернопіль",
        "Рівне",
        "Житомир",
        "Вінниця",
        "Черкаси",
        "Полтава",
        "Суми",
        "Чернігів",
        "Ужгород",
        "Кропивницький",
        "Маріуполь",
        "Краматорськ",
    ]

    random.seed(42)
    roads = [
        ("Київ", "Львів", random.randint(1, 10)),
        ("Київ", "Одеса", random.randint(1, 10)),
        ("Київ", "Харків", random.randint(1, 10)),
        ("Київ", "Дніпро", random.randint(1, 10)),
        ("Дніпро", "Запоріжжя", random.randint(1, 10)),
        ("Львів", "Луцьк", random.randint(1, 10)),
        ("Луцьк", "Київ", random.randint(1, 10)),
        ("Одеса", "Дніпро", random.randint(1, 10)),
        ("Київ", "Чернігів", random.randint(1, 10)),
        ("Київ", "Житомир", random.randint(1, 10)),
        ("Житомир", "Львів", random.randint(1, 10)),
        ("Львів", "Івано-Франківськ", random.randint(1, 10)),
        ("Івано-Франківськ", "Чернівці", random.randint(1, 10)),
        ("Тернопіль", "Чернівці", random.randint(1, 10)),
        ("Тернопіль", "Львів", random.randint(1, 10)),
        ("Тернопіль", "Хмельницький", random.randint(1, 10)),
        ("Хмельницький", "Вінниця", random.randint(1, 10)),
        ("Вінниця", "Київ", random.randint(1, 10)),
        ("Вінниця", "Ужгород", random.randint(1, 10)),
        ("Одеса", "Миколаїв", random.randint(1, 10)),
        ("Миколаїв", "Херсон", random.randint(1, 10)),
        ("Херсон", "Запоріжжя", random.randint(1, 10)),
        ("Запоріжжя", "Маріуполь", random.randint(1, 10)),
        ("Маріуполь", "Краматорськ", random.randint(1, 10)),
        ("Краматорськ", "Харків", random.randint(1, 10)),
        ("Харків", "Полтава", random.randint(1, 10)),
        ("Полтава", "Київ", random.randint(1, 10)),
        ("Суми", "Полтава", random.randint(1, 10)),
        ("Суми", "Харків", random.randint(1, 10)),
        ("Суми", "Чернігів", random.randint(1, 10)),
        ("Чернігів", "Полтава", random.randint(1, 10)),
        ("Ужгород", "Львів", random.randint(1, 10)),
        ("Кропивницький", "Дніпро", random.randint(1, 10)),
        ("Кропивницький", "Миколаїв", random.randint(1, 10)),
        ("Кропивницький", "Київ", random.randint(1, 10)),
        ("Черкаси", "Київ", random.randint(1, 10)),
        ("Черкаси", "Полтава", random.randint(1, 10)),
        ("Рівне", "Луцьк", random.randint(1, 10)),
        ("Рівне", "Тернопіль", random.randint(1, 10)),
    ]

    G.add_nodes_from(cities)
    G.add_weighted_edges_from(roads)
    return G


def dijkstra(graph, start):
    queue = [(0, start)]
    distances = {node: float("infinity") for node in graph.nodes}
    distances[start] = 0
    shortest_paths = {node: [] for node in graph.nodes}
    shortest_paths[start] = [start]

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, attributes in graph[current_node].items():
            weight = attributes["weight"]
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))
                shortest_paths[neighbor] = shortest_paths[current_node] + [neighbor]

    return distances, shortest_paths


def visualize_graph(graph, shortest_paths, start_node):
    pos = nx.spring_layout(graph)
    plt.figure(figsize=(12, 8))
    nx.draw(
        graph,
        pos,
        with_labels=True,
        node_size=700,
        node_color="lightblue",
        font_size=10,
        font_weight="bold",
    )
    labels = nx.get_edge_attributes(graph, "weight")
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=labels)

    for end_node, path in shortest_paths.items():
        if end_node != start_node:
            path_edges = list(zip(path, path[1:]))
            nx.draw_networkx_edges(
                graph, pos, edgelist=path_edges, edge_color="r", width=2
            )

    plt.title(f"Найкоротші шляхи з {start_node}")
    plt.show()


def run():
    G = create_graph()

    start_node = "Київ"
    distances, paths = dijkstra(G, start_node)

    print("Distances from", start_node)
    for node in distances:
        print(f"Distance to {node}: {distances[node]}")

    print("\nPaths from", start_node)
    for node in paths:
        print(f"Path to {node}: {' -> '.join(paths[node])}")

    visualize_graph(G, paths, start_node)


if __name__ == "__main__":
    run()
