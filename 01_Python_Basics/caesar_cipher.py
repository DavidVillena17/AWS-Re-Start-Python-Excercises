"""
Descripción: Implementación de un algoritmo de Cifrado César para encriptar y desencriptar mensajes utilizando funciones personalizadas.
"""

def suma (numero1, numero2):
    resultado = numero1 + numero2
    return resultado

a = input("Escriba un numero: ")
a = int(a)

b = input("Escriba otro numero: ")
b = int(b)

print(suma(a, b))


def get_double_alphabet(alphabet):
    double_alphabet = alphabet + alphabet
    return double_alphabet

def get_message():
    string_to_encrypt = input("Please enter a message to encrypt: ")
    return string_to_encrypt

def get_cipher_key():
    shift_amount = input("Please enter a key (whole number from 1-25): ")
    return shift_amount

def run_caesar_cipher_program():
    my_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    print(f'Alphabet: {my_alphabet}')

    my_alphabet2 = get_double_alphabet(my_alphabet)
    print(f'Alphabet2: {my_alphabet2}')
    my_message = get_message()
    print(my_message)
    my_cipher_key = get_cipher_key()
    print(my_cipher_key)

    my_encrypted_message = encrypt_message(my_message, my_cipher_key, my_alphabet2)
    print(f'Encrypted Message: {my_encrypted_message}')
    my_decrypted_message = decrypt_message(my_encrypted_message, my_cipher_key, my_alphabet2)
    print(f'Decypted Message: {my_decrypted_message}')

def encrypt_message(message, cipher_key, alphabet):
    encrypted_message = ""
    uppercase_message = ""
    uppercase_message = message.upper()

    for current_character in uppercase_message:
        position = alphabet.find(current_character)
        new_position = position + int(cipher_key)

        if current_character in alphabet:
            encrypted_message = encrypted_message + alphabet[new_position]
        else:
            encrypted_message = encrypted_message + current_character

    return encrypted_message

def decrypt_message(message, cipher_key, alphabet):
    decrypt_key = -1 * int(cipher_key)
    return encrypt_message(message, decrypt_key, alphabet)
run_caesar_cipher_program()