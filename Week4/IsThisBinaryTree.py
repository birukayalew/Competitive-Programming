""" Node is defined as
class node:
  def __init__(self, data):
      self.data = data
      self.left = None
      self.right = None
"""
ans=[]
def check_binary_search_tree_(root):
    trees(root)
    for i in range(len(ans)-1):
        if ans[i]>=ans[i+1]:
            return False
    return True
def trees(root):
    if root:
        trees(root.left)
        ans.append(root.data)
        trees(root.right)
