def diagonalDifference(arr):
    sum1 = 0
    sum2 = 0
    for i in range(0, len(arr)):
        sum1+=arr[i][i]
        sum2+=arr[i][len(arr)-1-i]
    return abs(sum1-sum2)
    
