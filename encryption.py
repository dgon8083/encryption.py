import random
import string

#our string of characters
chars = " " + string.punctuation + string.digits + string.ascii_letters
#turn our string of characters into a list
#making each character an individual element
chars = list(chars)
key = chars.copy()

#shuffles the key around
random.shuffle(key)

#ENCRYPT
plain_text = input("Enter a message to encrpty:")
cipher_text = ""

for letter in plain_text:
    index = chars.index(letter)
    cipher_text += key[index]

print(f"original message: {plain_text}")
print(f"encrypted message: {cipher_text}")

#DECRYPT
cipher_text = input("Enter the message to decrypt:")
plain_text =""

for letter in cipher_text:
    index = key.index(letter)
    plain_text += chars[index]

print(f"encrypted message: {cipher_text}")
print(f"original message: {plain_text}")