/**
 * @author Bhautik Bharadava
 */
let string = "Hello World";
let words = string.split(" ");
function print() {
  words.map(function(word) {
    console.log(word);
  });
}

print();
