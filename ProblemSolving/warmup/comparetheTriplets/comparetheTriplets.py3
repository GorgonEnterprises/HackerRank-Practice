def compareTriplets(a, b):
    arr = [0,0]
    for i in range(0,3):
        print("i=", i)
        if(a[i] > b[i]):
            arr[0]+=1
            print("a", a[i])
        if(b[i] > a[i]):
            arr[1]+=1
            print("b", b[i])
    return arr
    
