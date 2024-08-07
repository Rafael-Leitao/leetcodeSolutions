from binarytree import build

def maxDepth(root):
    if not root:
        return 0
    
    else:
        return 1 + max(maxDepth(root.left), maxDepth(root.right))
    

tree_list = [3,9,20,None,None,15,7]
root = build(tree_list)

print(maxDepth(root))