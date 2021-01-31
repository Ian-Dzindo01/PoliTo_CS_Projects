# This code was taken from: https://github.com/aladdinpersson/Algorithms-Collection-Python/blob/master/Algorithms/cryptology/vigenere_cipher/vigenere.py
# Tried writing my own code, but came up with a lot more complex solution, which is inferior to this one.

alphabet = "abcdefghijklmnopqrstuvwxyz"

letter_to_index = dict(zip(alphabet, range(len(alphabet))))
index_to_letter = dict(zip(range(len(alphabet)), alphabet))


message = input("Please enter the message you want encoded: ").strip()
key = input("Please enter the word that you want to use as a key: ").strip()


def encrypt(message, key):
    encrypted = ""
    split_message = [message[i : i + len(key)] for i in range(0, len(message), len(key))]

    for each_split in split_message:
       i = 0
       for letter in each_split:
           number = (letter_to_index[letter] + letter_to_index[key[i]]) % len(alphabet)       # this line is important to understand
           encrypted += index_to_letter[number]
           i += 1

    return encrypted



def decrypt(message, key):
    decrypted = ""
    split_message = [message[i : i + len(key)] for i in range(0, len(message), len(key))]

    for each_split in split_message:
       i = 0
       for letter in each_split:
           number = (letter_to_index[letter] - letter_to_index[key[i]]) % len(alphabet)       # this line is important to understand
           decrypted += index_to_letter[number]
           i += 1

    return decrypted


encrypted = encrypt(message, key)

print(encrypted)
print(decrypt(encrypted, key))

