#Original list
L1 = ['Hello', 'World', 18, 'Apple', None]
#Create a string list from original list
L2 = [x.lower() for x in L1 if isinstance(x,str) == True]
#Testing
print(L2)
if L2 == ['hello', 'world', 'apple']:
    print('Pass')
else:
    print('Fail')