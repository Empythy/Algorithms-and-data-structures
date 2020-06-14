class TreeNode(object):
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


def preOrderRecusive(root):
    if root:
        print(root.val)
        preOrderRecusive(root.left)
        preOrderRecusive(root.right)


def midOrderRecusive(root):
    if root:
        midOrderRecusive(root.left)
        print(root.val)
        midOrderRecusive(root.right)
def lastOrderRecusive(root):
    if root:
        lastOrderRecusive(root.left)
        lastOrderRecusive(root.right)
        print(root.val)
## 深度优先：  先序遍历： 根左右
#             中序遍历   左根右
#             后序遍历   左右根

## 广度优先

## 非递归的形式遍历
def preOrder(root):
    if root is None:
        return None
    stack = []
    tmpNode = root

    while stack or tmpNode:
        while tmpNode:
            print(tmpNode.val)
            stack.append(tmpNode)
            tmpNode = tmpNode.left
        node = stack.pop()
        tmpNode = node.right


def midOrder(root):
    if root is None:
        return None
    stack = []
    tmpNode = root

    while stack or tmpNode:
        while tmpNode:
            stack.append(tmpNode)
            tmpNode = tmpNode.left
        node = stack.pop()
        print(node.val)
        tmpNode = node.right

def lastOrder(root):
    if root is None:
        return None
    stack = []
    tmpNode = root

    while stack or tmpNode:
        ## 一直寻找到左子树 最左边
        while tmpNode:
            stack.append(tmpNode)
            print("压入", tmpNode.val)
            tmpNode = tmpNode.left

        node = stack[-1]
        tmpNode = node.right  ## 右孩子
        # 当最左边的节点没有右子树 才将根节点pop出
        if node.right is None:
            node = stack.pop()
            print("pop 出", node.val)
            while stack and node == stack[-1].right:
                node = stack.pop()
                print("pop 出", node.val)
                # print(node.val)

if __name__ == '__main__':

    t3 = TreeNode(3)
    t2 = TreeNode(2)
    t1 = TreeNode(1)
    t0 = TreeNode(0)
    t4 = TreeNode(4, right=t1)
    t5 = TreeNode(5, left=t0)
    t6 = TreeNode(6, left=t3, right=t2)
    t7 = TreeNode(7, left=t5, right=t4)
    t8 = TreeNode(8, left=t7, right=t6)




    # preOrderRecusive(t1)
    #
    # preOrder(t1)
    # midOrderRecusive(t1)
    # midOrder(t1)

    lastOrderRecusive(t8)
    print("*" * 30)
    lastOrder(t8)

