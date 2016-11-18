class Node:
  def __init__(self, data):
    self.data = data
    self.child = {}

  def append(self, title, child):
    self.child[title] = child


CEO = Node(('ceo', 1000))
CTO = ('cto', 100)
CFO = ('cfo', 10)
CEO.append('left child', CTO)
CEO.append('right child', CFO)

print(CEO.data)
print(' ', CEO.child['left child'])
print(' ', CEO.child['right child'])