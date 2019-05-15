def getTotalX(a, b):
    least = b[0]
    count = 0
    for each in b:
        if each < least:
            least = each
    
    for i in range(1,least+1):
        flag = 1
        for each in b:
            if each % i !=0:
                flag=0
                break
            for item in a:
                if i % item !=0:
                    flag=0
                    break
        if flag:
            count +=1
    return count
    
