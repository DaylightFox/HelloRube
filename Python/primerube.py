def is_prime(num):
    if abs(num) > 1:
        for i in range(2, n):
            if num % i == 0:
                return False
        return True
    else:
        return False


# Gather integer from user
user_num = input("Enter a positive integer: ")
if user_num.isdigit():
    real_user_num = int(user_num)
else:
    print("That's not a positive integer, let me fix that for you.\n")
    real_user_num = 0
    for char in user_num:
        real_user_num += ord(char)

# If Prime - Reverse string
if is_prime(real_user_num):
    print("Result: {0}".format(bytes.fromhex('48656c6c6f20576f726c6421').decode('utf-8')[::-1]))

# If not prime - print regular string
else:
    print("Result: {0}".format(bytes.fromhex('48656c6c6f20576f726c6421').decode('utf-8')))
