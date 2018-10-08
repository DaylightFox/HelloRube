# Print strings together with a +

puts "Example 1 "

a = "hello "
b = "world"

puts a + b 

puts "-----------------------------"
# Contatenate strings and variables with #{}

puts "Example 2 "

a = "world"

puts  "hello #{a}"

puts "-----------------------------"

# Loop through an array

puts "Example 3 "

a = ["h", "e", "l", "l", "o", " ", "w", "o", "r", "l", "d"]

a.each do |letter|
	puts letter
end

puts "-----------------------------"

# Print the array the way it is

puts "Example 4 "

p a 

puts "-----------------------------"

# use an object

puts "Example 5 "

class Word
	def initialize
		@h = "hello"
		@w = "world"
	end

	def display
		puts @h, @w 
	end
end 

a = Word.new

a.display				


puts "-----------------------------"

