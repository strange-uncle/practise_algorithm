
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.sum = 0
    
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        def middle_scan(n: TreeNode):
            if n is None:
                return
            middle_scan(n.left)
            if L <= n.val <= R:
                self.sum += n.val
            middle_scan(n.right)
    
        middle_scan(root)
        return self.sum

    def rangeSumBST_optimise(self, root: TreeNode, L: int, R: int) -> int:
        def middle_scan(n: TreeNode):
            if n is None:
                return
            if n.val > L:
                middle_scan(n.left)
            if n.val < R:
                middle_scan(n.right)
            if L <= n.val <= R:
                self.sum += n.val
                print('n.val is ', n.val)
                
        middle_scan(root)
        return self.sum


if __name__ == '__main__':
    """
    示例 1：

    输入：root = [10,5,15,3,7,null,18], L = 7, R = 15
    输出：32
    示例 2：

    输入：root = [10,5,15,3,7,13,18,1,null,6], L = 6, R = 10
    输出：23
    """
    rt = TreeNode(10)
    rt.left = TreeNode(5)
    rt.right = TreeNode(15)
    rt.left.left = TreeNode(3)
    rt.left.right = TreeNode(7)
    rt.right.left = None
    rt.right.right = TreeNode(18)
    
    L = 7
    R = 15
    search_bst = Solution()
    # print(search_bst.rangeSumBST(rt, L, R))
    print(search_bst.rangeSumBST_optimise(rt, L, R))
