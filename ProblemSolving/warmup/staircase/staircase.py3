def staircase(n):
    str=""
    for i in range(0, n):
        if i>0:
            str+="\n"
        for j in range(0, n):
            if j < n-i-1:
                str+=" "
            else:
                str+="#"
    print(str)
    
