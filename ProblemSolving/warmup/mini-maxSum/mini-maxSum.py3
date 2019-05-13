def miniMaxSum(arr):
    min=arr[0]
    max=arr[0]
    sum=0
    for each in arr:
        sum+=each
        if each > max:
            max=each
        if each<min:
            min=each
    print(sum-max, sum-min)
    
