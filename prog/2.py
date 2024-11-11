#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Система управления складом


class TreeNode:
    def __init__(self, item):
        self.item = item  # Товар
        self.left = None  # Левый узел
        self.right = None  # Правый узел


def find_item(node, target, depth, max_depth):
    # Проверяем, достигли ли мы конца дерева или максимальной глубины
    if node is None or depth > max_depth:
        return None

    # Проверяем, совпадает ли текущий узел с искомым товаром
    if node.item == target:
        return node

    # Поиск в левом поддереве
    left_result = find_item(node.left, target, depth + 1, max_depth)
    if left_result is not None:
        return left_result

    # Поиск в правом поддереве
    return find_item(node.right, target, depth + 1, max_depth)


# Пример использования
if __name__ == "__main__":
    # Создаем дерево
    root = TreeNode("Товар A")
    root.left = TreeNode("Товар B")
    root.right = TreeNode("Товар C")
    root.left.left = TreeNode("Товар D")
    root.left.right = TreeNode("Товар E")
    root.right.left = TreeNode("Товар F")
    root.right.right = TreeNode("Товар G")
    root.right.right.right = TreeNode("Товар T")

    # Определяем искомый товар и максимальную глубину
    target_item = "Товар T"
    max_depth = 3

    # Выполняем поиск
    result = find_item(root, target_item, 0, max_depth)

    # Выводим результат
    if result:
        print(f"Товар найден: {result.item}")
    else:
        print("Товар не найден в заданной глубине.")
