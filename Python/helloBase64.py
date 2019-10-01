import base64

string = "SGVsbG8gV29ybGQhCg=="

print(base64.b64decode(string).decode())
