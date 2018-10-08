// Ruby is a dependency for this JavaScript to run :)

var exec = require("child_process").exec;

exec("ruby ./Ruby/helloworld.rb", function(error, stdout, stderr) {
  console.log(stdout);
});
