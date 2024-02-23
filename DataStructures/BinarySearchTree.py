class BST:
    def _init_(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.data: # comparing with root
            if self.left is None: # can insert as left leaf node
                self.left = BST(value)
            else: # recursively insert to left subtree
                self.left.insert(value)
        else: # value > self.data
            if self.right is None: # can insert as right leaf node
                self.right = BST(value)
            else: # recursively insert to right subtree
                self.right.insert(value)

    def search(self, target):
        if self.data == target: # success
            return "Found"
        elif self.left is None and self.right is None: # unsuccessful / leaf
            return "Not found"
        elif target < self.data: # go left
            if self.left is None: # node with no left child or 1 right child
                return "Not found"
            else: # left subtree exists
                return self.left.search(target) # recursive 1 go left
        else: # target > self.data: # go right
            if self.right is None: # node with no right child or 1 left child
                return "Not found"
            else: # right subtree exists
                return self.right.search(target) # recursive 2 go right

    def inorder(self): # left root right -- sorted order, process left then root then right, root is in btwn (in)
        if self.left: # recursive 1: go left because left subtree exists
            self.left.inorder()
        print(self.data, end=' ') # anchor/terminating case -- middle
        if self.right: # recursive 2: go right because right subtree exists
            self.right.inorder()

    def preorder(self): # root left right -- root is in front (pre)
        print(self.data, end=' ') # anchor/terminating case -- first
        if self.left: # recursive 1: go left because left subtree exists
            self.left.preorder()
        if self.right: # recursive 2: go right because right subtree exists
            self.right.preorder()

    def postorder(self): # left right root -- root last (post)
        if self.left: # recursive 1: go left because left subtree exists
            self.left.postorder()
        if self.right: # recursive 2: go right because right subtree exists
            self.right.postorder()
        print(self.data, end=' ') # anchor/terminating case

    def reverse(self): # right root left
        if self.right: # recursive 2: go right because right subtree exists
            self.right.reverse()
        print(self.data, end=' ') # anchor/terminating case
        if self.left: # recursive 1: go left because left subtree exists
            self.left.reverse()

    def minimum(self):
        if self.left is None: # leftmost
            print(self.data)
        else:
            self.left.minimum()

    def maximum(self):
        if self.right is None: # rightmost
            print(self.data)
        else:
            self.right.maximum()

# main
bst = BST(50)
bst.insert(30)
bst.insert(80)
bst.insert(10)
bst.insert(40)
bst.insert(90)
bst.insert(60)
bst.insert(70)
bst.inorder()
print()
print(bst.search(50))
print(bst.search(90))
print(bst.search(20))
bst.preorder()
print()
bst.postorder()
print()
bst.reverse()
print()
bst.minimum()
bst.maximum()
