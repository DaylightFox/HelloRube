# Prints string using slice! from reverse
puts 'Example 1'

a = 'ybur olleh'
b =''

while !a.empty? do
  b += a.slice!(a.length - 1)
end

puts b

puts '############################'

# Using alphabet lookup
puts 'Example 2'

alphabet = ("a".."z").to_a
alphabet << " "

a = [7,4,11,11,14,26,17,20,1,24]
b = ''

a.each { |letter| b += alphabet[letter] }

puts b

puts '############################'
