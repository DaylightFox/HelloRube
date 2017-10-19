
class SayHello {
  constructor(message) {
    this.prefix = 'Hello';
    this.message = message || 'world';
    this.suffix = '!';
  }

  say() {
    console.log(this.prefix + ' ' + this.message + '' + this.suffix);
  }
}

(function (Factory, undefined) {
  var message = new Factory('Msmtotti');
  message.say();
})(SayHello);
