function func(...data) {
    let middleDict = {};
    for (let name of data) {
        let middle = name[1];
        
        if (name.length === 2) {
            middle = name[1]; 
        } else if (name.length === 4) {
            middle = name[2]; 
        }else if (name.length === 5) {
            middle = name[2]; 
        }

        if (!(middle in middleDict)) {
            middleDict[middle] = {
                num: 1,
                name: name
            };
        } else {
            middleDict[middle].num += 1;
        }
    }
    
    let isDisplay = false;
    for (let middle in middleDict) {
        let item = middleDict[middle];
        if (item.num === 1) {
            console.log(item.name);
            isDisplay = true;
            break;
        }
    }

    if (!isDisplay) {
        console.log("沒有");
    }
}

func("彭大牆", "陳王明雅", "吳明"); // print 彭大牆
func("郭靜雅", "王立強", "郭林靜宜", "郭立恆", "林花花"); // print 林花花
func("郭宣雅", "林靜宜", "郭宣恆", "林靜花"); // print 沒有
func("郭宣雅", "夏曼藍波安", "郭宣恆"); // print 夏曼藍波安
