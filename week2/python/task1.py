def find_and_print(messages, current_station):
    station  = ["Songshan", "Nanjing Sanmin","Taipei","Nanjing Fuxing","Songjiang Nanjing","Zhongshan","Beimen","Ximen","Xiaonanmen","Chiang Kai-Shek Memorial Hall","Guting","Taipower Building","Gongguan","Wanlong","Jingmei","Dapinglin","Qizhang","Xiaobitan", "no use", "Xindian City Hall","Xindian"] 
    cur_index = station.index(current_station)
    # print("cur_index= ", cur_index)

    min = 9999
    user = "xxx"
    for person, message in messages.items():
        m = message.split(" ")
        for mx in m:
            if(mx in station):
                person_idx = station.index(mx)
                # print(f"{person}: {person_idx}", min)
                if(abs(person_idx-cur_index)<min):
                    min = abs(person_idx-cur_index)
                    user=person
                #break
            
    print(f"{user}")

    
messages={
    "Leslie":"I'm at home near Xiaobitan station.",
    "Bob":"I'm at Ximen MRT station.",
    "Mary":"I have a drink near Jingmei MRT station.",
    "Copper":"I just saw a concert at Taipei Arena.",
    "Vivian":"I'm at Xindian station waiting for you."
}


find_and_print(messages,"Wanlong") # print Mary
find_and_print(messages,"Songshan") # print Copper
find_and_print(messages,"Qizhang") # print Leslie
find_and_print(messages,"Ximen") # print Bob
find_and_print(messages,"Xindian City Hall") # print Vivian

