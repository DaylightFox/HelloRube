const target = "Hello World";
var output = "";

for (var i = 0; i < target.length; i++){
  var char;

  while (char != target[i]){
    char = String.fromCharCode(Math.random() * 127);
  }

  output += char;
}

console.log(output);
