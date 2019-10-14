# Ruby command-line Hello World app
# With thanks to the Internet Anagram Server, https://wordsmith.org/anagram/
# Run 'ruby jumble_hello.rb'

def jumble(word)
  print word, "\r"
  sleep 0.7
  20.times do
    word = word.chars.shuffle.join
    print word, "\r"
    sleep 0.03
  end
end

def hello_world
  jumble('World Hello')
  jumble('Rolled Howl')
  jumble('Howled Roll')
  jumble('Howler Doll')
  jumble('Droll Whole')
  jumble('Lord Hell Ow')
  puts 'Hello World'.ljust(12) # some strings are 12 characters instead of 11
end

hello_world
