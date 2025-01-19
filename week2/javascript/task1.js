function findAndPrint(messages, currentStation) {
    const line1 = ["Songshan", "Nanjing Sanmin", "Taipei", "Nanjing Fuxing", "Songjiang Nanjing", 
                   "Zhongshan", "Beimen", "Ximen", "Xiaonanmen", "Chiang Kai-Shek Memorial Hall", 
                   "Guting", "Taipower Building", "Gongguan", "Wanlong", "Jingmei", "Dapinglin", "Qizhang"];
    const line2 = ["Xiaobitan"];
    const line3 = ["Xindian City Hall", "Xindian"];

    let curline = [];
    if (line1.includes(currentStation)) {
        curline = line1;
    } else if (line2.includes(currentStation)) {
        curline = line2;
    } else if (line3.includes(currentStation)) {
        curline = line3;
    }

    let minDistance = 9999;
    let user = "xxx";

    for (let person in messages) {
        const message = messages[person];
        const words = message.split(" ");

        for (let mx of words) {
            let personLine = [];
            if (line1.includes(mx)) {
                personLine = line1;
            } else if (line2.includes(mx)) {
                personLine = line2;
            } else if (line3.includes(mx)) {
                personLine = line3;
            } else {
                continue; 
            }

            let station = [];
            if (curline.length > personLine.length) {
                station = curline.concat(personLine);
            } else if (curline.length < personLine.length) {
                station = personLine.concat(curline);
            } else {
                station = [...curline];
            }

            const personIdx = station.indexOf(mx);
            const curIndex = station.indexOf(currentStation);

            if (Math.abs(personIdx - curIndex) < minDistance) {
                minDistance = Math.abs(personIdx - curIndex);
                user = person;
                break; 
            }
        }
    }

    console.log(user);
}

// Sample messages
const messages = {
    "Leslie": "I'm at home near Xiaobitan station.",
    "Bob": "I'm at Ximen MRT station.",
    "Mary": "I have a drink near Jingmei MRT station.",
    "Copper": "I just saw a concert at Taipei Arena.",
    "Vivian": "I'm at Xindian station waiting for you.",
};

// Test cases
findAndPrint(messages, "Wanlong");  // Expected: Mary
findAndPrint(messages, "Songshan"); // Expected: Copper
findAndPrint(messages, "Qizhang");  // Expected: Leslie
findAndPrint(messages, "Ximen");    // Expected: Bob
findAndPrint(messages, "Xindian City Hall"); // Expected: Vivian
