from python.data_structures.binary_tree import BinaryTree
from python.data_structures.queue import Queue



def breadth_first(tree):
    output = []
    queue = Queue()
    queue.enqueue(tree.root)

    if tree.root is None:
        return []

    while not queue.is_empty():
        current = queue.dequeue()
        output.append(current.value)
        if current.left:
            queue.enqueue(current.left)
        if current.right:
            queue.enqueue(current.right)
    return output

def breadth_first3(tree):
    list_ = []
    queue = Queue()
    queue.enqueue(tree.root)

    if not tree.root:
        return list_

    while not queue.is_empty():
        position = queue.dequeue()
        print(type(position))

        list_.append(position.value)

        if position.left:
            queue.enqueue(position.left)

        if position.right:
            queue.enqueue(position.right)
            print(position.right.value)
            print(str(queue))
            print(type(position.right))

    return list_


def breadth_first2(tree):
    result = []
    queue = [tree.root]
    if not tree.root:
        return result
    while queue:
        front = queue.pop(0)
        result.append(front.value)
        if front.left:
            queue.append(front.left)
        if front.right:
            queue.append(front.right)
    return result
