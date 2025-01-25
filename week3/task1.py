# parse data from URLs
import urllib.request 
import json
import csv
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
src_spot="https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment-1"
src_mrt="https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment-2"
spot_data=json.load(urllib.request.urlopen(src_spot))
mrt_data=json.load(urllib.request.urlopen(src_mrt))

spot_keys=spot_data["data"]["results"][0].keys()
mrt_keys=mrt_data["data"][0].keys()
key_match=list(set(spot_keys)&set(mrt_keys)) #find same key
spot_list=spot_data["data"]["results"]
mrt_list=mrt_data["data"]

# for first file
merged_result=[]
for dict_spot in spot_list:
    for dict_mrt in mrt_list:
        if dict_spot[key_match[0]]== dict_mrt[key_match[0]]: #use the first same key
            urls = dict_spot["filelist"].split("https://") 
            merged_dict={
                "SpotTitle": dict_spot["stitle"],
                "District": dict_mrt["address"][5:8],
                "Longitude": dict_spot["longitude"],
                "Latitude": dict_spot["latitude"],
                "ImageURL": "https://"+urls[1], #use the first jpg
            }
            merged_result.append(merged_dict)
# print(merged_result)

# output file in CSV format
with open("spot.csv","w",newline="",encoding="utf-8") as spot_csv:
    fieldnames=["SpotTitle","District","Longitude","Latitude","ImageURL"]
    data=csv.DictWriter(spot_csv, fieldnames=fieldnames)
    data.writerows(merged_result)


# for second file
mrt_record={}
for dict_mrt in mrt_list:
    mrt_record[dict_mrt["SERIAL_NO"]] = dict_mrt["MRT"]

mrt_result={}
for dict_spot in spot_list:
    spot_id=dict_spot[key_match[0]]
    spot_name=dict_spot["stitle"]
    spot_mrt=mrt_record[spot_id]
    if spot_mrt not in mrt_result:
        mrt_result[spot_mrt] = [] #初始化
    mrt_result[spot_mrt].append(spot_name)
print(mrt_result)

# output file in CSV format
with open("mrt.csv","w",newline="",encoding="utf-8") as mrt_csv:  
    data=csv.writer(mrt_csv)
    for mrt,spot in mrt_result.items():
        row = [mrt] + spot  
        data.writerow(row)

print("done")





    



