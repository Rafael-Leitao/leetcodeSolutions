from binarytree import build

def isBalanced(root):

    def dfs(root):
        if not root:
            return [True, 0]
        
        left = dfs(root.left)
        right = dfs(root.right)

        balanced = left[0] and right[0] and (abs(left[1] - right[1]) <= 1)

        return [balanced, (1 + max(left[1], right[1]))]
    
    return dfs(root)[0]


tree = [1,2,2,3,3,None,None,4,4]
root = build(tree)
print(isBalanced(root))
