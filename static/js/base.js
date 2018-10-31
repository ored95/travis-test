var getSolution = function (triplet) {
    // bad cases
    if (triplet.length === 0)
        document.getElementById("result").innerHTML = "err";

    // good cases
    var sides = triplet.sort((x, y) => (x - y));
    
    var delta = Math.pow(sides[0], 2) + Math.pow(sides[1], 2) - Math.pow(sides[2], 2);
    document.getElementById("result").innerHTML = (Math.abs(delta) < 1e-100) ?
        "Pythagore's triplet" :
        "Non-Pythagore's triplet";
}