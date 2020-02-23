# Create Stack using linkedlist, 
# Stack using Array is very easy so I am not considering here.

from  Problems.LinkedList import node

class Stack:
  def __init__(self):
    self.top = None
    self.bottom = None
    self.length = 0

  def push(self,value):
    newNode = node(value,None)
    if self.length == 0:
      self.top = self.bottom = newNode
    else:
      holdingTop = self.top
      self.top = newNode
      self.top.nextNode = holdingTop
    self.length += 1
    return True

  def peek(self):
    return self.top.value
  
  def pop(self):
    if self.isEmpty():
      return False
    topNode = self.top
    if self.top.nextNode is not None:
      self.top = self.top.nextNode
    else:
      self.top = self.bottom = None
    self.length -= 1
    return topNode.value

  def isEmpty(self):
    return self.length == 0

  def PrintAsLinkedList(self):
    if self.top is None:
      return None
    tempArr = []
    currentNode = self.top
    while currentNode.nextNode is not None:
        tempArr.append(str(currentNode.value))
        currentNode = currentNode.nextNode
    else:
        tempArr.append(str(currentNode.value))
    print(" --> ".join(tempArr))