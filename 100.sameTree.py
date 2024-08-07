from binarytree import build

def isSameTree(p, q):
    if not p and not q:
        return True
    
    if not p or not q or p.val != q.val:
        return False
    
    return (isSameTree(p.left, q.left) and isSameTree(p.right, q.right))


p = [1,2,3]
q = [1,2,3]
treeP = build(p)
treeQ = build(q)
print(isSameTree(treeP, treeQ))  # Output: True
