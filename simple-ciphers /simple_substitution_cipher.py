"""
NOTE:
This is a simple substitution cipher created for learning purposes.
It is NOT real encryption and should not be used for security.
"""
import random as rd
import string as st

chars = " " + st.punctuation + st.digits + st.ascii_letters

chars = list(chars)
key = chars.copy()
rd.shuffle(key)

#ENCRYPT
plain_text = input("Enter the message that need to encrypted : ")
cipher_text = ""
for letter in plain_text:
    index = chars.index(letter)
    cipher_text += key[index]
print(f"The Original Message   : {plain_text}")
print(f"The Decrypted Message  : {cipher_text}")
#DECRYPT
cipher_text = input("Enter the message that need to Decrypted : ")
plain_text = ""
for letter in cipher_text:
    index = key.index(letter)
    plain_text += chars[index]
print(f"The Encrypted Message  : {cipher_text}")
print(f"The Original Message  : {plain_text}")
