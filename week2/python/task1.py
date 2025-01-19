def find_and_print(messages, current_station):

    line1 = ["Songshan", "Nanjing Sanmin","Taipei","Nanjing Fuxing","Songjiang Nanjing","Zhongshan","Beimen","Ximen","Xiaonanmen","Chiang Kai-Shek Memorial Hall","Guting","Taipower Building","Gongguan","Wanlong","Jingmei","Dapinglin","Qizhang", ] 
    line2 = ["Xiaobitan"] 
    line3 = ["Xindian City Hall","Xindian"]
    
    cur_info = {}
    cur_info["line"] = "xxx"
    cur_info["index"] = 999

    curline = "xxx"
    if(current_station in line1):
       curline = line1
    elif(current_station in line2):
        curline = line2
    elif(current_station in line3):
        curline = line3

    min = 9999
    user = "xxx"
    for person, message in messages.items():
        m = message.split(" ")
        # print("m= ", m)
        for mx in m:
            personline = []
            if(mx in line1):
                personline = line1
            elif(mx in line2):
                personline = line2
            elif(mx in line3):
                personline = line3
            else:
                continue

            station = []
            if(len(curline)>len(personline)):
                station = curline + personline
            elif(len(curline)<len(personline)):
                station = personline + curline
            else:
                station = curline

            person_idx = station.index(mx)
            cur_index = station.index(current_station)
            if(abs(person_idx-cur_index)<min):
                min = abs(person_idx-cur_index)
                user=person
                break

         
    print(f"{user}")

    
messages={
    "Leslie":"I'm at home near Xiaobitan station.",
    "Bob":"I'm at Ximen MRT station.",
    "Mary":"I have a drink near Jingmei MRT station.",
    "Copper":"I just saw a concert at Taipei Arena.",
    "Vivian":"I'm at Xindian station waiting for you.",
}


find_and_print(messages,"Wanlong") # print Mary
find_and_print(messages,"Songshan") # print Copper
find_and_print(messages,"Qizhang") # print Leslie
find_and_print(messages,"Ximen") # print Bob
find_and_print(messages,"Xindian City Hall") # print Vivian
