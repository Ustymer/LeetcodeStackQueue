def tree_by_levels(node):
    if node is None:
        return []
    res = []
    qu = []
    qu.append(node)
    while qu:
        qu.reverse()
        now = qu.pop()
        qu.reverse()
        res.append(now.value)
        if now.left:
            qu.append(now.left)
        if now.right:
            qu.append(now.right)
    
    return res
