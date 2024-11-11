#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Node:
    def __init__(self, name, cost=0, left=None, right=None):
        self.name = name  # Название узла
        self.cost = cost  # Стоимость узла
        self.left = left  # Левый дочерний узел
        self.right = right  # Правый дочерний узел


class Problem:
    def __init__(self, root):
        self.root = root  # Корневой узел дерева


def limited_depth_dfs(
    node, target, max_depth, current_depth=0, current_cost=0, path=None
):
    if path is None:
        path = []

    # Добавляем текущий узел в путь и суммируем затраты
    path.append(node.name)
    total_cost = current_cost + node.cost

    # Если нашли целевой узел
    if node.name == target:
        return path.copy(), total_cost  # Копируем путь для сохранения результата

    # Если достигли максимальной глубины, возвращаем бесконечную стоимость
    if current_depth >= max_depth:
        path.pop()
        return None, float("inf")

    # Рекурсивный поиск в левом и правом дочернем узле
    left_path, left_cost = (None, float("inf"))
    if node.left:
        left_path, left_cost = limited_depth_dfs(
            node.left, target, max_depth, current_depth + 1, total_cost, path
        )

    right_path, right_cost = (None, float("inf"))
    if node.right:
        right_path, right_cost = limited_depth_dfs(
            node.right, target, max_depth, current_depth + 1, total_cost, path
        )

    # Удаляем текущий узел из пути для корректного возврата
    path.pop()

    # Возвращаем путь с минимальной стоимостью
    if left_cost < right_cost:
        return left_path, left_cost
    else:
        return right_path, right_cost


if __name__ == "__main__":
    # Создание дерева
    root = Node(
        "root",
        0,
        left=Node("A", 3, left=Node("A1", 1), right=Node("A2", 2)),
        right=Node("B", 2, left=Node("B1", 4), right=Node("B2", 3)),
    )

    # Инициализация задачи
    problem = Problem(root)

    # Выполнение поиска
    target = "A2"
    max_depth = 2
    path, cost = limited_depth_dfs(problem.root, target, max_depth)

    # Результат поиска
    if path:
        print(
            f"Наименее затратный путь к '{target}': {' -> '.join(path)}, с затратами: {cost}"
        )
    else:
        print(f"Комната '{target}' не найдена в пределах глубины {max_depth}")
