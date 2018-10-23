let greetingsEng = "Hello World!";
let greetingsHin = "नमस्ते दुनिया!";

function print(greetingsLang) {
  greetingsLang.split("").forEach( (c, index) => {
    setTimeout( () => {
      console.clear();
      console.log(greetingsLang.slice(0, index+1));
    }, index * 500);
  });
}

let greetingsJoined = greetingsEng + " " + greetingsHin;

print(greetingsJoined); 
