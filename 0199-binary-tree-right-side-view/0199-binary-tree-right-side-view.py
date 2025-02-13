class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        result= []
        queue = deque([root])
        while queue:
            for i in range(len(queue)):
                node = queue.pop()
                if node.left:
                    queue.appendleft(node.left)
                if node.right:
                    queue.appendleft(node.right)

            result.append(node.val)

        return result