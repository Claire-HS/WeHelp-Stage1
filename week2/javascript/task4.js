function getNumber(index) {
let cnt = Math.floor(index / 3) * 7;
    let x = index % 3;
    if (x === 1) {
        cnt += 4;
    } else if (x === 2) {
        cnt += 8;
    }
    console.log(cnt);
}
getNumber(1);  // print 4
getNumber(5);  // print 15
getNumber(10); // print 25
getNumber(30); // print 70
