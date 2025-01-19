function findAndPrint(messages, currentStation) {
    const line1 = ["Songshan", "Nanjing Sanmin", "Taipei", "Nanjing Fuxing", "Songjiang Nanjing", "Zhongshan", "Beimen", "Ximen", "Xiaonanmen", "Chiang Kai-Shek Memorial Hall", "Guting", "Taipower Building", "Gongguan", "Wanlong", "Jingmei", "Dapinglin", "Qizhang"];
    const line2 = ["Xiaobitan"];
    const line3 = ["Xindian City Hall", "Xindian"];

    let curLine = "xxx";
    if (line1.includes(currentStation)) {
        curLine = line1;
    } else if (line2.includes(currentStation)) {
        curLine = line2;
    } else if (line3.includes(currentStation)) {
        curLine = line3;
    }

    let min = 9999;
    let user = "xxx";

    for (let person in messages) {
        let message = messages[person];
        let m = message.split(" ");

        for (let mx of m) {
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
            if (curLine.length > personLine.length) {
                station = curLine.concat(personLine);
            } else if (curLine.length < personLine.length) {
                if (curLine === line2 && personLine === line1) {
                    station = [currentStation].concat(personLine.reverse());
                } else if (curLine === line3 && personLine === line1) {
                    station = [currentStation].concat(personLine.reverse());
                } else {
                    station = curLine.concat(personLine);
                }
            } else {
                station = curLine;
            }

            let personIdx = station.indexOf(mx);
            let curIndex = station.indexOf(currentStation);

            if (Math.abs(personIdx - curIndex) < min) {
                min = Math.abs(personIdx - curIndex);
                user = person;
            }

            break;
        }
    }

    console.log(user);
}


let messages = {
    "Leslie": "I'm at home near Xiaobitan station.",
    "Bob": "I'm at Ximen MRT station.",
    "Mary": "I have a drink near Jingmei MRT station.",
    "Copper": "I just saw a concert at Taipei Arena.",
    "Vivian": "I'm at Xindian station waiting for you."
};

findAndPrint(messages, "Wanlong"); // print Mary
findAndPrint(messages, "Songshan"); // print Copper
findAndPrint(messages, "Qizhang"); // print Leslie
findAndPrint(messages, "Ximen"); // print Bob
findAndPrint(messages, "Xindian City Hall"); // print Vivian



