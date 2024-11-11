#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v, weight):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append((v, weight))
        self.graph[v].append((u, weight))  # Для неориентированного графа

    def depth_first_search(self, start, goal, max_depth):
        visited = set()  # Множество для отслеживания посещенных узлов
        return self._dfs_helper(start, goal, 0, max_depth, visited)

    def _dfs_helper(self, current_node, goal, current_depth, max_depth, visited):
        # Если достигли максимальной глубины, возвращаем False
        if current_depth > max_depth:
            return False

        # Если достигли цели, возвращаем True
        if current_node == goal:
            return True

        # Помечаем текущий узел как посещенный
        visited.add(current_node)

        # Рекурсивно исследуем соседей
        for neighbor, _ in self.graph.get(current_node, []):
            if neighbor not in visited:
                if self._dfs_helper(
                    neighbor, goal, current_depth + 1, max_depth, visited
                ):
                    return True

        # Убираем узел из посещенных, чтобы позволить его повторное посещение в других ветвях
        visited.remove(current_node)
        return False


# Пример использования
if __name__ == "__main__":
    g = Graph()

    # Добавление рёбер в граф с весами (пример)
    g.add_edge(0, 1, 130)
    g.add_edge(0, 2, 120)
    g.add_edge(1, 3, 90)
    g.add_edge(3, 4, 185)
    g.add_edge(2, 4, 145)
    g.add_edge(4, 5, 300)

    start = 0  # Начальная вершина
    goal = 5  # Конечная вершина
    max_depth = 2  # Максимальная глубина поиска

    found = g.depth_first_search(start, goal, max_depth)

    if found:
        print(f"Путь найден от {start} до {goal} в пределах глубины {max_depth}.")
    else:
        print("Путь не найден в пределах заданной глубины.")
