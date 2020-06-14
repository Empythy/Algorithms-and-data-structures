class Solution(object):
    def longestUnivaluePath(self, root):
        self.ans = 0

        def tranverse(node): # 返回以node为首的单边
            if not node:
                return 0

            left_len = tranverse(node.left)
            right_len = tranverse(node.right)

            left_arrow, right_arrow = 0, 0

            if node.left and node.left.val == node.val:
                left_arrow = left_len + 1

            if node.right and node.right.val == node.val:
                right_arrow = right_len + 1

            self.ans = max(self.ans, left_arrow + right_arrow)

            return max(left_arrow, right_arrow)

        tranverse(root)
        return self.ans