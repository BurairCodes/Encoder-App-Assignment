import streamlit as st

key = {
 'a': 'hY3kL', 'b': 'mQ7Za', 'c': 'X2pNc', 'd': 'vR5yT', 'e': 'wF8oJ',
 'f': 'Lq1eM', 'g': 'zT4rD', 'h': 'Bx9Ug', 'i': 'dW6kP', 'j': 'N2cVo',
 'k': 'rM7Kw', 'l': 'pX3qA', 'm': 'Eo9Nz', 'n': 'Zf4rT', 'o': 'qJ1sY',
 'p': 'Km6Pa', 'q': 'Tb9Xw', 'r': 'Va4Ej', 's': 'Yt3Kn', 't': 'Ao8Mf',
 'u': 'We1Xr', 'v': 'Rn6Oz', 'w': 'Pc2Qa', 'x': 'Sm9Kt', 'y': 'Uz5Xp', 'z': 'Jv7Wq', ' ': 'Gk7Lm',
}

def encode(input_string):
    input_string = input_string.lower()  # Convert to lowercase
    encoded_string = ""
    for char in input_string:
        if char in key:
            encoded_string += key[char]
        else:
            encoded_string += char  # Keep the character unchanged if not in the key
    return encoded_string

def decode(encoded_string):
    decoded_string = ""
    key_reversed = {v: k for k, v in key.items()}  # Reverse the key dictionary

    for i in range(0, len(encoded_string), 5):
        chunk = encoded_string[i:i+5]
        if chunk in key_reversed:
            print(f"Decoding chunk: {chunk} to {key_reversed[chunk]}")
            decoded_string += key_reversed[chunk]

    return decoded_string

input_string = st.text_input("Enter text to encode:")
encode_button = st.button("Encode")
decode_button = st.button("Decode")


if encode_button:
    st.write("Encoding...")
    st.text_input("Encoded text:", value=encode(input_string), disabled=True)
if decode_button:
    st.write("Decoding...")
    st.text_input("Decoded text:", value=decode(input_string), disabled=True)
    


