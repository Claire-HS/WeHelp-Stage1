def get_number(index):
    cnt = index // 3 * 7
    x = index % 3
    if(x==1):
        cnt = cnt + 4
    elif(x==2):
        cnt = cnt + 8
    print (cnt)
    
get_number(1) # print 4
get_number(5) # print 15
get_number(10) # print 25
get_number(30) # print 70
