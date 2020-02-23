# Create Queue using Linked list is best option
# using Array, when you dequeue you have shift Array and reindex Array. so It will be O(n) operation. Otherside, Linked List you can just remove first node and next node will become head. it will be O(1) operation of dequeue

from Problems.LinkedList import node

class Queue:
  def __init__(self):
      self.first = self.last = None
      self.length = 0

  def enqueue(self, value):
      newNode = node(value, None)
      if self.length == 0:
          self.first = self.last = newNode
      else:
          self.last.nextNode = newNode
          self.last = newNode
      self.length += 1

  def dequeue(self):
      if self.length == 0:
          return False
      FirstNode = self.first
      self.first = FirstNode.nextNode
      self.length -= 1

      return FirstNode.value

  def peek(self):
      return self.first.value

  def isEmpty(self):
    if self.first is None:
      return True

  def PrintAsLinkedList(self):
    if self.isEmpty():
      print("Queue is Empty")
      return None
    tempArr = []
    currentNode = self.first
    while currentNode.nextNode is not None:
        tempArr.append(str(currentNode.value))
        currentNode = currentNode.nextNode
    else:
        tempArr.append(str(currentNode.value))
    print( "Length:",self.length,"::: ", " --> ".join(tempArr))
