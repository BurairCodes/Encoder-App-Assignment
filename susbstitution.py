def substitution_encoding(n, input_string):
    encoded_string = ""

    for i in range(len(input_string)):
        ord(input_string[i]) + n
        if ord(input_string[i]) + n > 126:
            encoded_string += chr(ord(input_string[i]) + n - 95)
        else:
            encoded_string += chr(ord(input_string[i]) + n)
    return encoded_string

def substitution_decoding(n, input_string):
    decoded_string = ""

    for i in range(len(input_string)):
        if ord(input_string[i]) - n < 32:
            decoded_string += chr(ord(input_string[i]) - n + 95)
        else:
            decoded_string += chr(ord(input_string[i]) - n)
    return decoded_string

print(substitution_encoding(3, "Hello World!"))
print(substitution_decoding(3, "Khoor#Zruog$")) # Output: Khoor#Zruog$
