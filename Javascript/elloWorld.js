// Usage: $ node HelloRube/Javascript/elloWorld.js Hello World

let input = "";
process.argv.forEach((val, index, array) => {
  if ([0, 1].indexOf(index) === -1) {
    if (index !== 2) {
      val = ` ${val}`;
    }
    input += val;
  }
});

const ALPHABET = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ ".split(
  ""
);

const transformTextCharacterToAlphabetIndex = array => {
  return new Promise((resolve, reject) => {
    const indexArray = array.map(character => {
      const index = ALPHABET.indexOf(character);
      if (index !== -1) {
        return index;
      }
    });
    resolve(indexArray);
  });
};

const transformAlphabetIndexToCharacterArray = array => {
  return new Promise((resolve, reject) => {
    const characterArray = array.map(index => {
      return ALPHABET[index];
    });
    resolve(characterArray);
  });
};

const convertToArray = text => {
  return new Promise((resolve, reject) => {
    resolve(text.split(""));
  });
};

const convertToString = text => {
  return new Promise((resolve, reject) => {
    resolve(text.join(""));
  });
};

class HelloWorld {
  constructor(text) {
    this.text = text;
  }

  async transform(initialText) {
    let promises = [
      convertToArray,
      transformTextCharacterToAlphabetIndex,
      transformAlphabetIndexToCharacterArray,
      convertToString
    ];
    let lastResult = initialText;
    for (let i = 0; i < promises.length; i++) {
      lastResult = await promises[i](lastResult);
    }
    return lastResult;
  }

  say() {
    if (this.text === "" || this.text === undefined) {
      console.log("You forgot to enter some text...");
      return;
    }
    this.transform(this.text)
      .then(text => console.log(text))
      .catch(error => console.log(error));
  }
}
new HelloWorld(input).say();
