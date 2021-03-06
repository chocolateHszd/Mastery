# O(N)
# O(h)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.stack = []
        while root:
            self.stack.append(root)
            root = root.left
        
    def next(self) -> int:
        """
        @return the next smallest number
        """
        if self.hasNext():
            node = self.stack.pop()
            val = node.val
            if node.right:
                node = node.right
                while node:
                    self.stack.append(node)
                    node = node.left
            return val
        return None
        

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        if not self.stack :
            return False
        return True


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()