cursor = 72
delta = [0,29,7,0,3,-79,55,24,3,-6,-8,-67]
result = []

delta.each {
  cursor += it
  result << whatMyChar(cursor)
}

println result.join()

def whatMyChar(ascii) {
  return (char) ascii
}
