# Prints string using slice! from reverse

puts "Example 1 "

a = '!ybuR olleH'
b =''

while !a.empty? do
  b += a.slice!(a.length - 1)
end

puts b

puts "-----------------------------"
