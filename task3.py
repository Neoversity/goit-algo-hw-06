import networkx as nx
import matplotlib.pyplot as plt
import random

def create_graph():
    G = nx.Graph()
    cities = [
        "Київ", "Львів", "Одеса", "Харків", "Дніпро", "Запоріжжя", "Луцьк", 
        "Херсон", "Миколаїв", "Чернівці", "Івано-Франківськ", "Тернопіль", 
        "Рівне", "Житомир", "Вінниця", "Черкаси", "Полтава", "Суми", "Чернігів", 
        "Ужгород", "Кропивницький", "Маріуполь", "Краматорськ"
    ]

    random.seed(42)
    roads = [
        ("Київ", "Львів", random.randint(1, 10)), ("Київ", "Одеса", random.randint(1, 10)), ("Київ", "Харків", random.randint(1, 10)), 
        ("Київ", "Дніпро", random.randint(1, 10)), ("Дніпро", "Запоріжжя", random.randint(1, 10)), ("Львів", "Луцьк", random.randint(1, 10)), 
        ("Луцьк", "Київ", random.randint(1, 10)), ("Одеса", "Дніпро", random.randint(1, 10)), ("Київ", "Чернігів", random.randint(1, 10)),
        ("Київ", "Житомир", random.randint(1, 10)), ("Житомир", "Львів", random.randint(1, 10)), ("Львів", "Івано-Франківськ", random.randint(1, 10)), 
        ("Івано-Франківськ", "Чернівці", random.randint(1, 10)), ("Тернопіль", "Чернівці", random.randint(1, 10)), 
        ("Тернопіль", "Львів", random.randint(1, 10)), ("Тернопіль", "Хмельницький", random.randint(1, 10)), 
        ("Хмельницький", "Вінниця", random.randint(1, 10)), ("Вінниця", "Київ", random.randint(1, 10)), ("Вінниця", "Ужгород", random.randint(1, 10)),
        ("Одеса", "Миколаїв", random.randint(1, 10)), ("Миколаїв", "Херсон", random.randint(1, 10)), ("Херсон", "Запоріжжя", random.randint(1, 10)), 
        ("Запоріжжя", "Маріуполь", random.randint(1, 10)), ("Маріуполь", "Краматорськ", random.randint(1, 10)), 
        ("Краматорськ", "Харків", random.randint(1, 10)), ("Харків", "Полтава", random.randint(1, 10)), ("Полтава", "Київ", random.randint(1, 10)), 
        ("Суми", "Полтава", random.randint(1, 10)), ("Суми", "Харків", random.randint(1, 10)), ("Суми", "Чернігів", random.randint(1, 10)), 
        ("Чернігів", "Полтава", random.randint(1, 10)), ("Ужгород", "Львів", random.randint(1, 10)), ("Кропивницький", "Дніпро", random.randint(1, 10)), 
        ("Кропивницький", "Миколаїв", random.randint(1, 10)), ("Кропивницький", "Київ", random.randint(1, 10)), 
        ("Черкаси", "Київ", random.randint(1, 10)), ("Черкаси", "Полтава", random.randint(1, 10)), ("Рівне", "Луцьк", random.randint(1, 10)), 
        ("Рівне", "Тернопіль", random.randint(1, 10))
    ]

    G.add_nodes_from(cities)
    G.add_weighted_edges_from(roads)
    return G

def run():
    G = create_graph()
    
    pos = nx.spring_layout(G)
    plt.figure(figsize=(12, 8))
    nx.draw(G, pos, with_labels=True, node_size=700, node_color="lightblue", font_size=10, font_weight="bold")
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.title("Транспортна мережа міст України з вагами")
    plt.show()

    def dijkstra_all_pairs_shortest_paths(graph):
        return dict(nx.all_pairs_dijkstra_path(graph))

    shortest_paths = dijkstra_all_pairs_shortest_paths(G)

    for start in shortest_paths:
        for end in shortest_paths[start]:
            print(f"Shortest path from {start} to {end}: {' -> '.join(shortest_paths[start][end])}")

if __name__ == "__main__":
    run()
