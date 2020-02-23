import json
class node:
    def __init__(self, value, nextNode):
        self.value = value
        self.nextNode = nextNode

    def asJson(self):
        return dict(
            value=self.value,
            nextNode=self.nextNode.asJson()
            if self.nextNode is not None else self.nextNode)


class LinkedList:
    def __init__(self, value):
        self.head = node(value, None)
        self.tail = self.head
        self.length = 1

    def append(self, value):
        mynode = node(value, None)
        self.tail.nextNode = mynode
        self.tail = mynode
        self.length += 1

    def prepend(self, value):
        newNode = node(value, self.head)
        self.head = newNode
        self.length += 1

    def remove(self, index):
        if index == 0:
            self.head = self.head.nextNode
            return True
        if index >= self.length:
            index = self.length - 1
        previousNode = self._TraverseToIndex(index - 1)
        currentNode = previousNode.nextNode
        if currentNode.nextNode is None:
            previousNode.nextNode = None
            self.tail = previousNode
        else:
            previousNode.nextNode = currentNode.nextNode
        self.length -= 1

    def findAt(self, index):
        if index == 0:
            return self.head.value
        elif index >= self.length - 1:
            return self.tail.value
        else:
            return self._TraverseToIndex(index).value

    def insert(self, index, value):
        if index >= self.length:
            return self.append(value)
        if index == 0:
            return self.prepend(value)
        newNode = node(value, None)
        previousNode = self._TraverseToIndex(index - 1)
        currentNode = previousNode.nextNode
        newNode.nextNode = currentNode
        previousNode.nextNode = newNode
        self.length += 1

    def _TraverseToIndex(self, index):
        idx = 0
        currentNode = self.head
        while idx != index:
            currentNode = currentNode.nextNode
            idx += 1
        return currentNode

    def reverse(self):
        if self.head.nextNode is None:
            return self.head
        first = self.head
        self.tail = self.head
        second = first.nextNode
        while second is not None:
            temp = second.nextNode
            second.nextNode = first
            first = second
            second = temp
        self.head.nextNode = None
        self.head = first

    def AsJson(self):
        return json.dumps( dict(
            head=self.head.asJson(),
            tail=self.tail.asJson(),
            length=self.length))

    def PrintAsLinkedList(self):
        tempArr = []
        currentNode = self.head
        while currentNode.nextNode is not None:
            tempArr.append(str(currentNode.value))
            currentNode = currentNode.nextNode
        else:
            tempArr.append(str(currentNode.value))
        print(" --> ".join(tempArr))
