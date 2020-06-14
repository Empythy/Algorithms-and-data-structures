"""
给定一个二叉树，它的每个结点都存放着一个整数值。

找出路径和等于给定数值的路径总数。
路径不需要从根节点开始，也不需要在叶子节点结束，但是路径方向必须是向下的（只能从父节点到子节点）
二叉树不超过1000个节点，且节点数值范围是 [-1000000,1000000] 的整数
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/path-sum-iii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None



class Solution2:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        '''如果没有根节点，整个返回值应该为0，没有路径'''
        if not root:
            return 0
        '''
        self.dfs(root, sum)：这个方法是判断以当前点为起点往下是否有path，也就是path的数量，返回值应该是0或1
        self.pathSum(root.left, sum)：对于左节点我依然要考虑以它为起点往下判断
        self.pathSum(root.right, sum)：同上，于是，此时的sum是不变化的，仍然为初始值
        '''
        return self.dfs(root, sum) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)

    def dfs(self, root, path):
            if not root:
                return 0
            '''每一次都要减去当前层的节点值'''
            path -= root.val
            '''
            (1 if path==0 else 0)：说明找到了路径
            self.dfs(root.left, path) self.dfs(root.right, path)：
              此时path更新过，这是因为当前点既可以往左走找path，也可以往右走，是或的关系，只要有一边找到了路径，最终结果都会为1
            '''
            return (1 if path == 0 else 0) + self.dfs(root.left, path) + self.dfs(root.right, path)
