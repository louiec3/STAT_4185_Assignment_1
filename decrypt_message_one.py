cipher = {
    'a':'v',
    'b':'h',
    'c':'r',
    'd':'j',
    'e':'t',
    'f':'x',
    'g':'s',
    'h':'a',
    'i':'e',
    'j':'f',
    'k':'b',
    'l':'n',
    'm':'o',
    'n':'i',
    'o':'g',
    'p':'l',
    'q':'m',
    'r':'z',
    's':'q',
    't':'u',
    'u':'c',
    'v':'k',
    'w':'d',
    'x':'p',
    'y':'y',
    'z':'w',
    ' ': '}',
    '\n': '^',
    ',': '5',
    '!': '[',
    ':':'-',
    ')':'*',
    '.': '%' 
}

with open("encrypted_message_one.txt", 'r') as f:
    encrypted_message = f.readline()

print(encrypted_message)

# Write code below
reverse_cipher = {v:k for k,v in cipher.items()}

decrypted_message = ''
# Loop chacters in message and check if the character is within the 
# reverse_cipher. If it is, add the reverse value to the string. If it is not,
# add the current character.
for c in encrypted_message:
    if c in reverse_cipher:
        decrypted_message += reverse_cipher[c]
    else:
        decrypted_message += c

print(decrypted_message)
