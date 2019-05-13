def birthdayCakeCandles(ar):
    max=ar[0]
    count=0
    for each in ar:
        if each > max:
            max=each
            count=1
        elif each == max:
            count+=1
    return count
    
