### Checklist
# Ensure you have node installed
# Ensure Javascript/elloWorld.js exists

puts 'Executing elloWorld.js'

msg = 'Hello Ruby (from Javascript) world!'
js_file_path = './Javascript/elloWorld.js'
cmd = "node #{js_file_path} \"#{msg}\""
output = `#{cmd}`

puts output
