var getSolution = function (triplet) {
    // bad cases
    if (triplet.length === 0)
        return "err";

    // good cases
    var sides = triplet.sort((x, y) => (x - y));

    return ("Hello World");

    //var delta = Math.pow(sides[0], 2) + Math.pow(sides[1], 2) - Math.pow(sides[2], 2);
    //return (Math.abs(delta) < 1e-100) ?
    //    "Pythagore's triplet" :
    //    "Non-Pythagore's triplet";
}

var printKhui = function (triplet) {
    if (triplet.length === 3)
        return "err";
    return "KHUI";
    //if (parseFloat(triplet[0]) > 0)
    //    return ;
    //else return "Haxui";
}