/*** Author: Eduardo Quintanilha  
 **  Code for contribute on Hacktoberfest in HelloRube repository  
 **  URL: https://github.com/DaylightFox/HelloRube
 **
 **  Explain: The code randomizer a list of numbers and find
 **  your respective letter on ASCII code table.
 **  Finally printing 'Hello World!' on output;
 **/

const hello = 'Hello World!';
let text = '';
let pos = 0;

function sleep(ms) {
    return new Promise(resolve => {
        setTimeout(resolve, ms)
    })
}
const main = async () => {
    while (text !== hello) {
        await sleep(150);
        let charCode = Math.floor(Math.random() * 127);
        let letter = String.fromCharCode(charCode);
        if (hello[pos] == letter) {
            text += letter;
            pos++;
            console.log(`\nFound one => ${letter}`);
            console.log(`String: ${text}`);
        }
    }
    return text;
}
main().then((res) => console.log(`\nFinally,\n${res}\n`));