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
from Problems.LinkedList import LinkedList
myLinkedList = LinkedList(10)
myLinkedList.append(15)
myLinkedList.append(16)
myLinkedList.prepend(1)
myLinkedList.insert(1, 3)
myLinkedList.insert(0, 0)
myLinkedList.insert(100, 30)  ## it will just append value if index bigger
myLinkedList.insert(5, 20)

#print(myLinkedList.AsJson())
myLinkedList.PrintAsLinkedList()

myLinkedList.remove(myLinkedList.length - 2)  ## removing
myLinkedList.PrintAsLinkedList()
myLinkedList.remove(1)  ## removing
myLinkedList.PrintAsLinkedList()
myLinkedList.remove(myLinkedList.length - 1)  ## removing
myLinkedList.PrintAsLinkedList()
print(myLinkedList.findAt(3))
print("Reverse")
myLinkedList.reverse()
myLinkedList.PrintAsLinkedList()
