from collections import defaultdict, deque

# דוגמה לגרף בעצורים
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []


# דוגמה לעץ
#           1
#         / | \
#        2  3  4
#       /|\
#      5 6 7
root = TreeNode(1)
root.children = [TreeNode(2), TreeNode(3), TreeNode(4)]
root.children[0].children = [TreeNode(5), TreeNode(6), TreeNode(7)]


#-------------------------------------------------------------------------BFS graph

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)

    while queue:
        vertex = queue.popleft()
        print(vertex, end=" ")

        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)


#-------------------------------------------------------------------------BFS Tree


def bfs_tree(root):
    if not root:
        return

    visited = set()
    queue = deque([root])
    visited.add(root)

    while queue:
        node = queue.popleft()
        print(node.value, end=" ")

        for child in node.children:
            if child not in visited:
                visited.add(child)
                queue.append(child)


#-------------------------------------------------------------------------DFS graph

def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    print(start, end=" ")
    visited.add(start)
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)


#-------------------------------------------------------------------------DFS Tree

def dfs_tree(node, visited=None):
    if visited is None:
        visited = set()
    print(node.value, end=" ")
    visited.add(node)
    for child in node.children:
        if child not in visited:
            dfs_tree(child, visited)


#-------------------------------------------------------------------------run


print("BFS for graph:")
bfs(graph, 'A')
print("\n")
print("\nBFS for Tree:")
bfs_tree(root)
print("\n")
print("\nDFS for graph:")
dfs(graph, 'A')
print("\n")
print("\nDFS for Tree:")
dfs_tree(root)