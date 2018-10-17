str1 = "0b110100001100101011011000110110001101111"
str2 = "0b0111011101101111011100100110110001100100"

def convertBits(bits, encoding='utf-8', errors='surrogatepass'):
    n = int(bits, 2)
    #return n.to_bytes((n.bit_length() + 7) // 8, 'big').decode(encoding, errors) or '\0'
    return n.to_bytes((n.bit_length() + 7) // 8, 'big').decode()

print(convertBits(str1) + ', ' + convertBits(str2) + "!")
