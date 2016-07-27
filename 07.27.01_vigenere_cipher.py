# https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher

PLAINTEXT = 'ATTACKATDAWN'
KEY = 'LEMON'

def vigenere_cipher_func(key, message):

    message = message.lower()
    key = key.lower()

    cipher_message = ''
    key_value = 0

    for char in message:
        if ord(char) >= 97 and ord(char) < 134:
            mi = ord(char) - 97
            ki = ord(key[key_value % len(key)])
            ci = (mi + ki - 97) % 26 + 97
            cipher_message += chr(ci)
            key_value += 1
        else:
            cipher_message += char

    return cipher_message.upper()

def vigenere_decipher_func(key, message):
    
    message = message.lower()
    key = key.lower()

    plain_messages = ''
    key_value = 0

    for char in message:
        if ord(char) >= 97 and ord(char) < 134:
            ci = ord(char) - 97
            ki = ord(key[key_value % len(key)]) - 97
            mi = (ci - ki) % 26 + 97
            plain_messages += chr(mi)
            key_value += 1
        else:
            plain_messages += char

    return plain_messages.upper()

crypto_text = vigenere_cipher_func(KEY, PLAINTEXT)
decrypto_text = vigenere_decipher_func(KEY, crypto_text)

# tests
print(PLAINTEXT, ' + ', KEY, ' >> ', crypto_text)
print(crypto_text, ' - ', KEY, ' >> ', decrypto_text)


