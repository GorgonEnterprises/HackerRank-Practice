def countApplesAndOranges(s, t, a, b, apples, oranges):
    rapp=0
    rora=0
    for each in apples:
        if each + a >=s and each + a <=t:
            rapp+=1
    for each in oranges:
        if each + b >=s and each + b <=t:
            rora+=1
    print(rapp, rora, sep="\n")
    
