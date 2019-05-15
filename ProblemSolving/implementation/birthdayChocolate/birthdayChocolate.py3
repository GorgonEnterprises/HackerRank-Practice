def breakingRecords(scores):
    min = scores[0]
    max = scores[0]
    res = [0,0]
    for each in scores:
        if each > max:
            max = each
            res[0]+=1
        elif each < min:
            min = each
            res[1]+=1
    return res
    
