# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        res = []
        def search(root, target, path):
            if not root:
                return
            path += [root]
            if root.val == target.val:
                res.append(path.copy())
            for child in [root.left, root.right]:
                search(child, target, path)
                # search(root.right, target, path)
            path.pop()

        search(root, p, [])
        search(root, q, [])
        p_path = res[0]
        # print(p_path)
        q_path = res[1]
        # print(q_path)
        ans = None
        while p_path and q_path and p_path[0] == q_path[0]:
            ans = p_path[0]
            p_path.pop(0)
            q_path.pop(0)
        return ans


    def lowestCommonAncestor2(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        self.ans = None
        def recurse_tree(current_node):

            # If reached the end of a branch, return False.
            if not current_node:
                return False

            # Left Recursion
            left = recurse_tree(current_node.left)

            # Right Recursion
            right = recurse_tree(current_node.right)

            # If the current node is one of p or q
            mid = current_node == p or current_node == q

            # If any two of the three flags left, right or mid become True.
            if mid + left + right >= 2:
                self.ans = current_node

            # Return True if either of the three bool values is True.
            return mid or left or right

        # Traverse the tree
        recurse_tree(root)
        return self.ans


def create_tree():
    l = [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]
    n = len(l)
    data = []
    for item in l:
        if item != None:
            data.append(TreeNode(item))
        else:
            data.append(None)

    for i in range(n):
        left = 2 * i + 1
        right = 2 * i + 2
        if data[i] != None:
            if left < n:
                data[i].left = data[left]
            if right < n:
                data[i].right = data[right]
    return data[0]

def pre_order(root):
    if not root:
        print("None")
        return
    print(root.val)
    if root.left:
        pre_order(root.left)
    if root.right:
        pre_order(root.right)
root = create_tree()
# pre_order(root)

s = Solution()
res = s.lowestCommonAncestor(root, p=TreeNode(5), q=TreeNode(1))
print(res.val)






