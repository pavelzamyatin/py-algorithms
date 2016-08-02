# https://en.wikipedia.org/wiki/Caesar_cipher

# int 0..25
KEY = 5

TEXT = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras nibh nisl, suscipit sed erat at, vulputate porttitor dolor. Etiam auctor augue id quam tempus placerat. Curabitur interdum ullamcorper dapibus. Fusce mattis condimentum mauris, ut condimentum turpis porttitor quis. Nunc vitae hendrerit urna, vehicula malesuada tortor. Praesent dictum sit amet orci id lacinia. Proin ut quam nunc. Duis sit amet rutrum nibh. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos.'

def cezar_cipher_func(key, message):

    message = message.lower()

    cipher_message = ''

    for char in message:
        if ord(char) >= 97 and ord(char) < 134:
            mi = ord(char) - 97
            ci = (mi + key) % 26 + 97
            cipher_message+=chr(ci) 
        else:
            cipher_message+=char

    return cipher_message

# tests
c_text = cezar_cipher_func(KEY, TEXT)
u_text = cezar_cipher_func(21, c_text)

print(c_text)
print(u_text)
