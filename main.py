import time
t0 = time.time()
####SumOf Pair
# import random
# #from Problems import SumofPair

# randomArray = [random.randrange(0, 100) for item in range(10000)]

#print(SumofPair.SumOfPairInSet(randomArray,170000000000000))

# Print Time of function

###===========================================
##Reverse String
# from Problems.Reverse import Reverse

# makeReverse = Reverse()
# str ="Dhaval Patel"
# print(makeReverse.reverse(str))

# print(int(time.time() - t0))

###------------------------------------------------
## Merge sorted array
# from Problems.MergeSortedArray import MergeSortedArray

# objMergeSortedArray = MergeSortedArray()
# #print(objMergeSortedArray.DoMergeSortedArray([19,8,9],[5,12,10]))
# print(objMergeSortedArray.AnotherWay([7,8,9,20,25,28,29,30,35,36,38,39,40],[5,10,12,15,16,19]))

###=================================================================

## Custom Hash Table ****
# from Problems.HashTable import HashTable

# myHashTable = HashTable(2)
# myHashTable.setValue('grapes',10000)
# myHashTable.setValue('apples',54)
# print(myHashTable.getValue('grapes'))

#####=========================================================

## First Recurring char

# from Problems.FirstRecuringChar import FirstRecur

# findRecur = FirstRecur()
# print(findRecur.findFirstRecur([2,5,1,2,3,5,1,2,4]))

##============================================================

## Linked List
# from Problems.LinkedList import LinkedList
# myLinkedList = LinkedList(10)
# myLinkedList.append(15)
# myLinkedList.append(16)
# myLinkedList.prepend(1)
# myLinkedList.insert(1, 3)
# myLinkedList.insert(0, 0)
# myLinkedList.insert(100, 30)  ## it will just append value if index bigger
# myLinkedList.insert(5, 20)

# #print(myLinkedList.AsJson())
# myLinkedList.PrintAsLinkedList()

# myLinkedList.remove(myLinkedList.length - 2)  ## removing
# myLinkedList.PrintAsLinkedList()
# myLinkedList.remove(1)  ## removing
# myLinkedList.PrintAsLinkedList()
# myLinkedList.remove(myLinkedList.length - 1)  ## removing
# myLinkedList.PrintAsLinkedList()
# print(myLinkedList.findAt(3))
# print("Reverse")
# myLinkedList.reverse()
# myLinkedList.PrintAsLinkedList()

###==============================================================
###++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
###==============================================================

## Stacks
# from Problems.Stack import Stack
# myStack = Stack()
# myStack.push('google')
# myStack.push('Amazon')
# myStack.push('Tcs')

# myStack.PrintAsLinkedList()

# print(myStack.pop())
# myStack.PrintAsLinkedList()

# print(myStack.pop())
# myStack.PrintAsLinkedList()

# print(myStack.pop())
# myStack.PrintAsLinkedList()

##==================================================================
# Queue
# from Problems.Queue import Queue

# myQueue = Queue()
# myQueue.enqueue('a')
# myQueue.enqueue('b')
# myQueue.enqueue('c')
# myQueue.PrintAsLinkedList()

# print('dequeue value => ',myQueue.dequeue())
# print('dequeue value => ',myQueue.dequeue())
# print('dequeue value => ',myQueue.dequeue())
# print('dequeue value => ',myQueue.dequeue())

# myQueue.PrintAsLinkedList()

##==============================================================

## Priority Queue
# from Problems.PriorityQueue import PriorityQueue

# myPQ = PriorityQueue()
# myPQ.enqueue("Sumit", 2) 
# myPQ.enqueue("Gourav", 1)
# myPQ.enqueue("Piyush", 1)
# myPQ.enqueue("Sunny", 2)
# myPQ.enqueue("Sheru", 3)

# myPQ.printQueue()

# print(myPQ.dequeue())
# print(myPQ.dequeue())
# myPQ.printQueue()


##==================================================================
# Binary Tree
#from Problems.BinaryTree import BinaryTree

# myTree = BinaryTree()
# myTree.insert(55)
# myTree.insert(10)
# myTree.insert(79)
# myTree.insert(47)
# myTree.insert(26)
# myTree.insert(41)
# myTree.insert(43)
# myTree.insert(50)
# myTree.insert(51)
# myTree.insert(49)
# myTree.insert(48)

# myTree.printTreeAsJson()
# print('============LOOKUP=================')
# print(myTree.lookup(47).asJson())
# print('============Remove=================')
# myTree.remove(47)
# myTree.remove(26)
# myTree.remove(10)
# myTree.printTreeAsJson()

##=================================================================================
#Graph

## Please follow this graph we are takinig as example hex
## https://visualgo.net/en/graphds

# from Problems.Graph import Graph

# myGraph = Graph()
# myGraph.addVertex('0')
# myGraph.addVertex('1')
# myGraph.addVertex('2')
# myGraph.addVertex('3')
# myGraph.addVertex('4')
# myGraph.addVertex('5')
# myGraph.addVertex('6')

# myGraph.addEdge('0','1')
# myGraph.addEdge('0','2')
# myGraph.addEdge('1','2')
# myGraph.addEdge('1','3')
# myGraph.addEdge('2','4')
# myGraph.addEdge('3','4')
# myGraph.addEdge('4','5')
# myGraph.addEdge('5','6')

# # Print Adjacency List
# myGraph.showConnections()
