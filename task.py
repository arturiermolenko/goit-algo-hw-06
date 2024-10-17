import random

import matplotlib.pyplot as plt
import networkx as nx

from algorithms import dfs, bfs, dijkstra

G = nx.Graph()

# Вузли (зупинки)
stops = [
    "Подусівка",
    "Тероборони",
    "Ріпкинська",
    "Любецька",
    "Мазепи",
    "Миру",
    "Перемоги",
    "Молодчого",
    "Шевченка",
    "Діагностичний центр",
    "Автозавод",
    "Залізничний вокзал",
    "Міська лікарня № 2",
    "Грушевського",
    "Лук’яненка",
    "Тарновського",
    "Гетьмана Полуботка",
    "П’ятницька",
]
G.add_nodes_from(stops)

# Ребра (шляхи між зупинками)
edges = [
    ("Подусівка", "Тероборони"),
    ("Тероборони", "Ріпкинська"),
    ("Ріпкинська", "Любецька"),
    ("Любецька", "Мазепи"),
    ("Мазепи", "Миру"),
    ("Миру", "Перемоги"),
    ("Перемоги", "Молодчого"),
    ("Молодчого", "Шевченка"),
    ("Шевченка", "Діагностичний центр"),
    ("Мазепи", "Автозавод"),
    ("Автозавод", "Залізничний вокзал"),
    ("Залізничний вокзал", "Гетьмана Полуботка"),
    ("Міська лікарня № 2", "Грушевського"),
    ("Грушевського", "Лук’яненка"),
    ("Лук’яненка", "Шевченка"),
    ("Шевченка", "Тарновського"),
    ("Тарновського", "Гетьмана Полуботка"),
    ("Гетьмана Полуботка", "П’ятницька"),
    ("П’ятницька", "Перемоги"),
    ("Перемоги", "Миру"),
    ("Миру", "Автозавод"),
]
for edge in edges:
    G.add_edge(edge[0], edge[1], weight=random.randint(1, 10))

pos = nx.spring_layout(G)
plt.figure(figsize=(12, 10))
nx.draw(
    G,
    pos,
    with_labels=True,
    node_color="lightblue",
    font_weight="bold",
    node_size=2000,
    font_size=10,
    edge_color="gray",
)
labels = nx.get_edge_attributes(G, "weight")
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.title("Граф з вагами ребер")
plt.show()

num_nodes = G.number_of_nodes()
num_edges = G.number_of_edges()
degree_of_nodes = dict(G.degree())

print(f"Кількість вершин: {num_nodes}")
print(f"Кількість ребер: {num_edges}")
print("Ступінь кожної вершини:")
for node, degree in degree_of_nodes.items():
    print(f"{node}: {degree}")

print("-" * 100)

start = "Подусівка"
goal = "Залізничний вокзал"

dfs_path = dfs(G, start, goal)
print(f"Шлях від '{start}' до '{goal}' за допомогою DFS: {dfs_path}")


bfs_path = bfs(G, start, goal)
print(f"Шлях від '{start}' до '{goal}' за допомогою BFS: {bfs_path}")

print("\nПорівняння:")
print(f"DFS знайшов шлях: {dfs_path}")
print(f"BFS знайшов шлях: {bfs_path}")

print("-" * 100)

distances, paths = dijkstra(G, start)
print(f"Найкоротші відстані від '{start}' до всіх вершин:")
for node, distance in distances.items():
    print(f"{node}: {distance} (шлях: {' -> '.join(paths[node])})")
