
#Google Question
#Given an array = [2,5,1,2,3,5,1,2,4]:
#It should return 2

#Given an array = [2,1,1,2,3,5,1,2,4]:
#It should return 1

#Given an array = [2,3,4,5]:
#It should return undefined

class FirstRecur:
  def __inti__(self):
    pass

#  Time complexity: O(n), Space Comple: O(n)
  def findFirstRecur(self,sourceArray):
    sourceDict = dict()

    for char in sourceArray:
      if sourceDict.get(char,None) is not None:
        return char
      else:
        sourceDict[char] = True
    return None
    