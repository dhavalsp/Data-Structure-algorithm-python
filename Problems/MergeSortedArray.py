
class MergeSortedArray:
  
  def __init__(self):
    pass
  
  def __SortingArray(self,sourceArray):
    if type(sourceArray) is list:
      sourceArray.sort()
      return sourceArray
    else: 
      return None
  
  def DoMergeSortedArray(self,leftArray,rightArray):
    if type(leftArray) is list and type(rightArray) is list:
      self.__sorted = self.__SortingArray(leftArray + rightArray)
      return self.__sorted
    else:
      print('Both arguments have to be array')

  def AnotherWay(self,leftArray,rightArray):
    self.__leftln = len(leftArray)
    self.__rightln = len(rightArray)
    sortedMerge = []
    self.__i =0
    self.__j=0
    while self.__i < self.__leftln and self.__j < self.__rightln:
      if(leftArray[self.__i] < rightArray[self.__j]):
        sortedMerge.append(leftArray[self.__i])
        self.__i += 1
      else:
        sortedMerge.append(rightArray[self.__j])
        self.__j += 1
    else:
      sortedMerge += leftArray[self.__i:] if self.__j >= self.__rightln-1 else  rightArray[self.__j:]
    return sortedMerge

        

      
    