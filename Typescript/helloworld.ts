
function helloworld(): string {
    let letter: number = 0;
    let message: string = "";
    while (true) {
        if (letter == 0) {
            message += "H";
        } else if (letter == 1) {
            message += "e";
        } else if (letter == 2) {
            message += "l";
        } else if (letter == 3) {
            message += "l";
        } else if (letter == 4) {
            message += "o";
        } else if (letter == 5) {
            message += " ";
        } else if (letter == 6) {
            message += "W";
        } else if (letter == 7) {
            message += "o";
        } else if (letter == 8) {
            message += "r";
        } else if (letter == 9) {
            message += "l";
        } else if (letter == 10) {
            message += "d";
        } else if (letter == 11) {
            message += "!";
        } else {
            break;
        }
        letter++;
    }
    return message;
}

console.log(helloworld());