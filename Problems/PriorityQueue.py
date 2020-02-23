## Resource Reference for more details
#https://www.geeksforgeeks.org/implementation-priority-queue-javascript/
# here we have use Array but we should use linked list to avoid Array shift cost
# Please checkout Queue class for linked list concept


class QElement:
  def __init__(self,value,priority):
    self.value = value
    self.priority = priority


class PriorityQueue:
  def __init__(self):
    self.data = []

  def enqueue(self,value,priority):
    newQ = QElement(value,priority)
    for idx,q in enumerate(self.data):
      if(q.priority > newQ.priority):
        self.data = self.data[:idx] + [newQ] + self.data[idx:]
        break
    else:
      self.data.append(newQ)
    

  def dequeue(self):
    front = self.front()
    self.data = self.data[1:]
    return front 

  def front(self):
    return self.data[0].value if len(self.data) > 0 else None

  def isEmpty(self):
    return len(self.data) == 0

  def printQueue(self):
    print("-->".join([self.data[i].value for i in range(len(self.data))]))

  def Count(self):
    return len(self.data)