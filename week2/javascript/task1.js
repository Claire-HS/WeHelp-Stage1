function findAndPrint(messages, currentStation) {
    const station  = ["Songshan", "Nanjing Sanmin","Taipei","Nanjing Fuxing","Songjiang Nanjing","Zhongshan","Beimen","Ximen","Xiaonanmen","Chiang Kai-Shek Memorial Hall","Guting","Taipower Building","Gongguan","Wanlong","Jingmei","Dapinglin","Qizhang","Xiaobitan", "no use", "Xindian City Hall","Xindian"];
    const curIndex = station.indexOf(currentStation);
    
    let minDistance = 999;
    let closestUser = "xxx";
    for (const [person, message] of Object.entries(messages)) {
        const words = message.split(" ");

        for (const word of words) {
            if (station.includes(word)) {
                const personIdx = station.indexOf(word);
                const distance = Math.abs(personIdx - curIndex);
                if (distance < minDistance) {
                    minDistance = distance;
                    closestUser = person;
                }
                break;
            }
        }
    }
    console.log(closestUser);
}

// Test cases
const messages = {
    "Leslie": "I'm at home near Xiaobitan station.",
    "Bob": "I'm at Ximen MRT station.",
    "Mary": "I have a drink near Jingmei MRT station.",
    "Copper": "I just saw a concert at Taipei Arena.",
    "Vivian": "I'm at Xindian station waiting for you."
};

findAndPrint(messages, "Wanlong");  // print Mary
findAndPrint(messages, "Songshan");  // print Copper
findAndPrint(messages, "Qizhang");  // print Leslie
findAndPrint(messages, "Ximen");    // print Bob
findAndPrint(messages, "Xindian City Hall");  // print Vivian
