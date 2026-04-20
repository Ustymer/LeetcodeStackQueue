# Pre-order traversal
def pre_order(node):
    res = []
    def find(node):
        if node is None:
            return None
        res.append(node.data)
        find(node.left)
        find(node.right)
    find(node)
    return res

# In-order traversal
def in_order(node):
    res = []
    def find(node):
        if node is None:
            return None
        find(node.left)
        res.append(node.data)
        find(node.right)
    find(node)
    return res

# Post-order traversal
def post_order(node):
    res = []
    def find(node):
        if node is None:
            return None
        find(node.left)
        find(node.right)
        res.append(node.data)
    find(node)
    return res

