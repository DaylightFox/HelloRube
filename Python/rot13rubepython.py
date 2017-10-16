# This passes a coded string into a function that decodes rot13 messages and returns the decoded message
def decode(secret):
    result = ""
    for char in secret:
        c = ord(char)
        if 64 < c < 78:
            result += chr(c + 45)
        elif c >= 78:
            result += chr(c + 19)
        else:
            result += char
    return result


secret = ["U", "R", "Y", "Y", "B", " ","J", "B", "E", "Y", "Q","!"]
print(decode(secret))
