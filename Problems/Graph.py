
# class Node:
#   def __init__(self,value):
#     self.value = value
#     self.connectedNode = []

#   def getValue(self):
#     return self.value

#   def AddConnection(self,node):
    
#     if node is not None:
#       self.connectedNode.append(node)
    

  
class Graph:
  def __init__(self):
    self.numberOfNodes = 0
    self.adjacentList = dict()

  def addVertex(self,nodeValue):
    self.adjacentList[nodeValue] = []
    self.numberOfNodes += 1
  
  def addEdge(self,node1,node2):
    if (node1,node2) != (None,None):
      self.adjacentList[node1].append(node2)
      if(node2 in self.adjacentList):
        self.adjacentList[node2].append(node1)

  
  def showConnections(self):
    allNodes = self.adjacentList.keys()
    for node in allNodes:
      nodeConnections = self.adjacentList[node]
      connections = ""
      for vertex in nodeConnections:
        connections += vertex + " "
      print(node,"-->",connections)