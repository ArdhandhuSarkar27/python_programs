num = [1,4,9,16,25,36,49,81,100,49]
x = 49
idx = 0
for ele in num:
    if ele==x:
        print("Element found at index",idx)
    '''break can be used here if you immediately want to stop
     right after getting the first element x which is 49 else
      you can just continue with this program '''
    idx+=1
