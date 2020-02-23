import json

#Class of Node for Binary Tree
class Node:
  def __init__(self,value):
    self.value = value
    self.leftNode = None
    self.rightNode = None
  
  def asJson(self):
    mydict = dict(value=self.value,leftNode=self.leftNode.asJson() if self.leftNode is not None else None,rightNode=self.rightNode.asJson() if self.rightNode is not None else None)
    return mydict
  
  # check if node is leaf node
  def isLeaf(self):
    return (self.leftNode,self.rightNode) == (None,None)
  
# Class of Binary Tree
# We have assume => Value will be only int 
class BinaryTree:
  def __init__(self):
    self.root = None
    self.count = 0
  
  # Insert value in Tree
  def insert(self,value):
    if self.root is None:
      self.root = Node(value)

    currentNode = self.root
    while True:
      if value < currentNode.value:
        if currentNode.leftNode is None:
          currentNode.leftNode = Node(value)
          break
        else:
          currentNode = currentNode.leftNode
      elif value > currentNode.value:
        if currentNode.rightNode is None:
          currentNode.rightNode = Node(value)
          break
        else:
          currentNode  = currentNode.rightNode
      else:
        return None
    self.count += 1

  """
  insight Lookup method retun lookup node with Parent of that node to utilize in remove function and many more operation.
  """
  def __insightLookup(self,value):
    if self.root is None:
      return False
    currentNode = self.root
    parentOfCurrentNode = None
    while True:
      if value < currentNode.value:
        parentOfCurrentNode = currentNode
        currentNode = currentNode.leftNode
      elif value > currentNode.value:
          parentOfCurrentNode = currentNode
          currentNode  = currentNode.rightNode
      elif value == currentNode.value:
        return (currentNode,parentOfCurrentNode)

  # Lookup node will return from __insightLookup tuple at 0 index
  def lookup(self,value):
    return self.__insightLookup(value)[0]

  # To remove node and adjust Tree structure
  def remove(self,value):
    if self.root is None:
      return False
    currentNode, ParentOfCurrentNode = self.__insightLookup(value)
    
    if currentNode.isLeaf():
      if ParentOfCurrentNode.value - currentNode.value > 0:
        ParentOfCurrentNode.leftNode = None
      else:
        ParentOfCurrentNode.rightNode = None
    elif currentNode.rightNode is not None:
        if currentNode.rightNode.isLeaf() or currentNode.rightNode.leftNode is None:
          #ParentOfCurrentNode.rightNode = currentNode.rightNode
          if ParentOfCurrentNode.value - currentNode.value > 0:
            ParentOfCurrentNode.leftNode = currentNode.rightNode
          else:
            ParentOfCurrentNode.rightNode = currentNode.rightNode
        else:
          if ParentOfCurrentNode.value - currentNode.value > 0:
            if currentNode.leftNode is not None:
              ParentOfCurrentNode.leftNode = currentNode.leftNode
            else:  
              ParentOfCurrentNode.leftNode = currentNode.rightNode
          else:
            tempNode = currentNode.rightNode
            tempParentNode = currentNode
            while tempNode.leftNode is not None:
              tempParentNode = tempNode
              tempNode = tempNode.leftNode
            tempNode.leftNode = currentNode.leftNode
            tempNode.rightNode = currentNode.rightNode
            tempParentNode.leftNode = None
            ParentOfCurrentNode.rightNode = tempNode
    elif currentNode.leftNode is not None and currentNode.rightNode is None:
      if ParentOfCurrentNode.value - currentNode.value > 0:
        ParentOfCurrentNode.leftNode = currentNode.leftNode
      else:
        ParentOfCurrentNode.rightNode = currentNode.leftNode
  
  def printTreeAsJson(self):
    if self.root is not None:
      print(json.dumps(self.root.asJson()))
    else:
      print("Empty Tree")



