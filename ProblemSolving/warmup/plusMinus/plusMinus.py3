def plusMinus(arr):
    pos=0
    neg=0 
    zer=0
    for each in arr:
        if each > 0:
            pos+=1
        elif each < 0:
            neg+=1
        else:
            zer+=1
    pos/=len(arr)
    neg/=len(arr)
    zer/=len(arr)
    print("{:f}\n{:f}\n{:f}".format(pos, neg, zer))
    
