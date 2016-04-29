# Binary Search Tree
# Create a BST and insert elements and print all tree traversal


class BSTNode(object):
    """
    Class to create a Binary Search Tree Node.
    """
    def __init__(self, key, left=None, right=None):
        self.left = left
        self.right = right
        self.key = key
        self.inlist = []
        self.prelist = []
        self.postlist = []

    def insert(self, node, key):
        if node is None:
            return BSTNode(key)
        elif key < node.key:
            node.left = self.insert(node.left, key)
        elif key > node.key:
            node.right = self.insert(node.right, key)
        return node

    def inorder(self, root):
        self.inlist = []
        return self.inorderUtil(root)

    def inorderUtil(self, root):
        if root:
            self.inorderUtil(root.left)
            self.inlist.append(root.key)
            self.inorderUtil(root.right)
        return self.inlist


    def preorder(self, root):
        self.inlist = []
        return self.preorderUtil(root)

    def preorderUtil(self, root):
	if root:
	    self.inlist.append(root.key)
	    self.preorderUtil(root.left)
	    self.preorderUtil(root.right)
	return self.inlist

    def postorder(self, root):
        self.inlist = []
        return self.postorderUtil( root)

    def postorderUtil(self, root):
    	if root:
            self.postorderUtil(root.left)
            self.postorderUtil(root.right)
            self.inlist.append(root.key)
	return self.inlist    
