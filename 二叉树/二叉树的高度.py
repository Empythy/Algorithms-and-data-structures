class TreeNode():
    def __init__(self, val):
        self.val = int(val)
        # print("正在构造", val)
        self.left = None
        self.right = None

def traverse_tree(root):
    if root is None:
        print("None")
        return
    print(root.val)
    traverse_tree(root.left)
    traverse_tree(root.right)

def read_data(n):
    data = {}
    root = None
    # input_data = [
    #     "0 1",
    #     "0 2",
    #     "1 3",
    #     "1 4"
    # ]
    # n = len(input_data)
    i = 1
    while i < n:
        s = input()
        if s == "":
            break
        parent, child = s.split(' ')
        if not parent in data:
            item = TreeNode(parent)
            if len(data) == 0:
                root = item
            data[parent] = item
        if not child in data:
            data[child] = TreeNode(child)
        # 构造子树
        if data[parent].left is None:
            data[parent].left = data[child]
        else:
            data[parent].right = data[child]
        i += 1
    return root

def height_of_tree(root):
    if root is None:
        return 0
    queue = [(root, 1)]
    depth = None
    while queue:
        node, depth = queue.pop(0)
        # print(node.val, depth)
        if node.left:
            queue.append((node.left, depth + 1))
        if node.right:
            queue.append((node.right, depth + 1))
    return depth

if  __name__ == "__main__":
    n = int(input())
    if n == 1:
        print(1)
    if n >= 2:
        root = read_data(n)
    # traverse_tree(root)
        res = height_of_tree(root)
        print(res)