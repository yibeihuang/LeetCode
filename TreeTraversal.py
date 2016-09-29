# tree traversal

## preorder
# as an external function that takes a binary tree as a parameter.
def preorder(tree):
	if tree:
		print(tree.getRootVal())
		preorder(tree.getLeftChild())
		preorder(tree.getRightChild())

# as a method of the BinaryTree class
def preorder(self):
	print(self.key)
	if self.LeftChild:
		self.LeftChild.preorder()
	if self.RightChild:
		self.RightChild.preorder()

## inorder
def inorder(tree):
  if tree != None:
      inorder(tree.getLeftChild())
      print(tree.getRootVal())
      inorder(tree.getRightChild())

## postorder
def postorder(tree):
	if tree:
		postorder(tree.getLeftChild())
		postorder(tree.getRightChild())
		print(tree.getRootVal())
