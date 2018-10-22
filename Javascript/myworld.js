function Greeting(){}
Greeting.prototype.sayhi= function(){
    console.log("Hello");
};

function Human(){ }
Human.prototype = Object.create(Greeting.prototype);
Human.prototype.constructor = Human;

Human.prototype.toworld = function(){
    console.log("World");
}

let john = new Human();
john.sayhi();
john.toworld();
