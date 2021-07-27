# Create a iterator to find out min and max number in a list, return in tuple
def findMinAndMax(L):
    if L == []:
        return(None, None)
    else:
        max = L[0]
        min = L[0]
        for x in L:
            if x > max:
                max = x
            if x < min:
                min = x
        return(min,max)

#Testing results
if findMinAndMax([]) != (None,None):
    print('testing faillure')
elif findMinAndMax([7]) != (7,7):
    print('testing faillure')
elif findMinAndMax([7,1]) != (1,7):
    print('testing faillure')
elif findMinAndMax([7,1,3,9,5]) != (1,9):
    print('testing faillure')
else:
    print('testing success!')

