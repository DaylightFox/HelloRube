import os

necessary_letters = list("hello world.")

completed_string = ""

for func in os.environ:
    if completed_string == "".join(necessary_letters):
        break

    for letter in necessary_letters:
        try:
            completed_string += func.__doc__[list(func.__doc__).index(letter)]
        except ValueError:
            break

print(completed_string)
