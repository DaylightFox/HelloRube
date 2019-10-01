dictionary = {0: 'A "Hello, World!" program generally is a computer program that outputs o',
              1: 'r displays the message "Hello, World!". Such a program is very simple in most programming languages, ',
              2: 'and is often used to illustrate the basic syntax of a programming language. It is often the first program wr',
              3: 'itten by people learning to code. The phrase has been used in various deviations in punctuation and casing, ',
              4: 'such as the presence of the comma and exclamation mark, and the capitalization of the leading H and W. Some dev',
              5: 'ices limit the format to specific variations, such as all-capitalized versions on syste',
              6: 'ms that support only capital letters, while some esoteric programming languages may have to print a slightly mo',
              7: 'dified string. For example, the first non-trivial Malbolge program printed "HEllO WORld", this having been determi',
              8: 'ned to be good enough. Variations in spirit exist as well. Functional programming languages, such as Lisp, M',
              9: 'L and Haskell, tend to substitute a factorial program for Hello, World, as functional programming em',
              10: 'phasizes recursive techniques.[1]'}

# print(''.join(list(dictionary.values())))

output = ''.join([chr(len(s)) for s in list(dictionary.values())])

if __name__ == '__main__':
    print(output[:5] + ' ' + output[5: ])
