import streamlit as st
import random as rd

from susbstitution import substitution_encoding, substitution_decoding




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

    for i in range(0, len(encoded_string), ):
        chunk = encoded_string[i:i+5]
        if chunk in key_reversed:
            print(f"Decoding chunk: {chunk} to {key_reversed[chunk]}")
            decoded_string += key_reversed[chunk]

    return decoded_string

# Streamlit App
st.title("Text Encoder/Decoder")

# Encoding
select_box = st.selectbox("Select an encoding variant", ["Substitution", "Key-Based"])

if select_box == "Substitution":
    n = st.number_input("Enter a number for substitution encoding", min_value=1, max_value=100, value=3)
    input_string = st.text_input("Enter the string to encode")
    st.write(substitution_encoding(n, input_string))

if select_box == "Key-Based":
    input_string = st.text_input("Enter the string to encode")
    st.write(encode(input_string))

select_box2 = st.selectbox("Select an decoding variant", ["Substitution", "Key-Based"])

if select_box2 == "Substitution":
    n = st.number_input("Enter a number for substitution decoding", min_value=1, max_value=100, value=3)
    input_string = st.text_input("Enter the string to decode")
    st.write(substitution_decoding(n, input_string))

elif select_box2 == "Key-Based":
    input_string = st.text_input("Enter the string to decode")
    st.write(decode(input_string))

    


