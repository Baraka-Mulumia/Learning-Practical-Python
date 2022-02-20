alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def encrypt(plain_text, shift_amount):
    cipher_text = ""
    for letter in plain_text:
        position = alphabet.index(letter)
        new_position = position + shift_amount

        if new_position >= 26:
            new_position = new_position - 26

        cipher_text += alphabet[new_position]

    print(f"the encoded text is  {cipher_text}")


# encrypt(plain_text=text, shift_amount=shift)

def decrypt(cipher_text, shift_amount):
    plain_text = ""
    for letter in cipher_text:
        position = alphabet.index(letter)
        new_position = position - shift_amount
        plain_text += alphabet[new_position]

    print(f"the decrypted text is  {plain_text}")


# decrypt(plain_text=text, shift_amount=shift)


def caesar_cipher():
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    if direction == "encode":
        encrypt(plain_text=text, shift_amount=shift)
    elif direction == "decode":
        decrypt(cipher_text=text, shift_amount=shift)
    else:
        print("You chose a wrong direction")


caesar_cipher()
