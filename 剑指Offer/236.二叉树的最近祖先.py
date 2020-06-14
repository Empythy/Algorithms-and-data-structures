"""
由于lowestCommonAncestor(root, p, q)的功能是找出以root为根节点的两个节点p和q的最近公共祖先。 我们考虑：
如果p和q分别是root的左右节点，那么root就是我们要找的最近公共祖先
如果root是None，说明我们在这条寻址线路没有找到，我们返回None表示没找到
我们继续在左右子树执行相同的逻辑。
如果左子树没找到，说明在右子树，我们返回lowestCommonAncestor(root.right, p , q)
如果右子树没找到，说明在左子树，我们返回lowestCommonAncestor(root.left, p , q)
如果左子树和右子树分别找到一个，我们返回root

作者：fe-lucifer
链接：https://leetcode-cn.com/problems/er-cha-shu-de-zui-jin-gong-gong-zu-xian-lcof/solution/chao-jian-dan-di-gui-pythonjavascript-by-azl397985/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root or root.val == p.val or root.val == q.val:
            return root
        l = self.lowestCommonAncestor(root.left, p, q)
        r = self.lowestCommonAncestor(root.right, p, q)
        if l and r: return root
        if l:
            return l
        if r:
            return r


class Solution2:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        res = []
        def search(root, target, path):
            if not root:
                return
            path += [root]
            if root.val == target.val:
                res.append(path.copy())
                return
            search(root.left, target, path)
            search(root.right, target, path)
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