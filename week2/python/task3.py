def func(*data):
    middle_dict = {}
    for i in range(0, len(data),1):
        name = data[i]
        
        middle = name[1]
        if(len(name)==2):
           middle = name[1]
        elif(len(name)==4):
            middle = name[2]
        elif(len(name)==5):
            middle = name[2]

        if(middle) not in middle_dict:
            middle_dict[middle] = {}
            middle_dict[middle]["num"] = 1
            middle_dict[middle]["name"] = name
        else:
            middle_dict[middle]["num"] = middle_dict[middle]["num"] + 1
    
    is_dislay = False
    for middle, item in middle_dict.items():
        if(item["num"]==1):
            print(item["name"])
            is_dislay = True
            break
    if(not is_dislay):
        print("沒有")

func("彭大牆","陳王明雅","吳明") # print 彭大牆
func("郭靜雅","王立強","郭林靜宜","郭立恆","林花花") # print 林花花
func("郭宣雅","林靜宜","郭宣恆","林靜花") # print 沒有
func("郭宣雅","夏曼藍波安","郭宣恆") # print 夏曼藍波安
