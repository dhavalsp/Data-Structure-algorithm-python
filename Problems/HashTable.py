# BEST Case of Big O of HashTable
# search O(1) 
# Insert O(1)
# lookup O(1)
# delete O(1)



class HashTable:

  def __init__(self,ArraySize):
    self.__data = [[] for i in range(ArraySize) ] 
  
  def __gethash(self,key):
    self.__hash = 0
    for idx, char in enumerate(key):
      self.__hash = (self.__hash + ord(char) * idx) % len(self.__data)
    return self.__hash
  
  def setValue(self,key,value):
    self.__Adrs = self.__gethash(key)
    self.__data[self.__Adrs].append([key,value])
    
  def getValue(self,key):
    print(self.__data)
    self.__Adrs = self.__gethash(key)
    for bucket in self.__data[self.__Adrs]:
      if(bucket[0] == key):
        return bucket
    
  
