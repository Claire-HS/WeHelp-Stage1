record = {
    "John":[],
    "Bob":[],
    "Jenny": []
}
def book(consultants, hour, duration, criteria):
    sorted_consultants = consultants
    if(criteria=="price"):
        sorted_consultants = sorted(consultants, key=lambda x: x["price"])
    if(criteria=="rate"):
        sorted_consultants = sorted(consultants, key=lambda x: -x["rate"])
    
    no_pass_cnt = 0
    for c in sorted_consultants:
        # print(c[t"name"])
        is_pass = True
        # 計算預約時間
        for d in range(0, duration, 1):
            h = hour + d
            if h in record[c["name"]]:
                is_pass = False
                break
        
        if(is_pass):
            for d in range(0, duration, 1):
                h = hour + d
                record[c["name"]].append(h)
            print(c["name"])
            is_pass = False
            break
        else: 
            no_pass_cnt = no_pass_cnt + 1

    if(no_pass_cnt==3): 
        print("No Service")
      
consultants=[
    {"name":"John","rate":4.5,"price":1000},
    {"name":"Bob","rate":3,"price":1200},
    {"name":"Jenny","rate":3.8,"price":800}
]
book(consultants, 15, 1,"price") # Jenny
book(consultants, 11, 2,"price") # Jenny
book(consultants, 10, 2,"price") # John
book(consultants, 20, 2,"rate") # John
book(consultants, 11, 1,"rate") # Bob
book(consultants, 11, 2,"rate") # No Service
book(consultants, 14, 3,"price") # John