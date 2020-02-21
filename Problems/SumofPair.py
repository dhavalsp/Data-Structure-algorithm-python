#32 time as result
def SumofPair(numArray, arrsum):
    for i in range(len(numArray)):
        for j in range(i + 1, len(numArray)):
            if numArray[i] + numArray[j] == arrsum:
                return True
    return False


def SumOfPairInSet(numsets, arrsum):
    myset = set(numsets)
    for num in myset:
        if arrsum - num in myset:
            return True
    return False


#print(SumofPair(randomArray,170000000000000))
