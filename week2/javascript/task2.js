const record = {
    "John": [],
    "Bob": [],
    "Jenny": []
};
function book(consultants, hour, duration, criteria) {
    let sortedConsultants = consultants;
    if (criteria === "price") {
        sortedConsultants = consultants.slice().sort((a, b) => a.price - b.price);
    }
    if (criteria === "rate") {
        sortedConsultants = consultants.slice().sort((a, b) => b.rate - a.rate);
    }
    let noPassCnt = 0;
    for (let c of sortedConsultants) {
        let isPass = true;
        for (let d = 0; d < duration; d++) {
            let h = hour + d;
            if (record[c.name].includes(h)) {
                isPass = false;
                break;
            }
        }
        if (isPass) {
            for (let d = 0; d < duration; d++) {
                let h = hour + d;
                record[c.name].push(h);
            }
            console.log(c.name);
            break; 
        } else {
            noPassCnt++;
        }
    }
    if (noPassCnt === 3) {
        console.log("No Service");
    }
}

const consultants = [
    {"name": "John", "rate": 4.5, "price": 1000},
    {"name": "Bob", "rate": 3, "price": 1200},
    {"name": "Jenny", "rate": 3.8, "price": 800}
];

book(consultants, 15, 1, "price");  // Jenny
book(consultants, 11, 2, "price");  // Jenny
book(consultants, 10, 2, "price");  // John
book(consultants, 20, 2, "rate");   // John
book(consultants, 11, 1, "rate");   // Bob
book(consultants, 11, 2, "rate");   // No Service
book(consultants, 14, 3, "price");  // John
