with open("encrypted_message_two.txt", 'r') as f:
    encrypted_message = f.readline()

# Write Code Here

# Make a list of the even indexes of the encrypyted text
# Make a list of the odd indexes of the encrypyted text
# Reverse the odd index list
even_index = encrypted_message[::2]
odd_index_rev = encrypted_message[1::2][::-1]

decrypted_message = ''
x = 0

# Loop elements and append the even_index list then the odd_index_reverse to 
# build the message.
for i in enumerate(encrypted_message):
    if x < len(odd_index_rev):
        decrypted_message += even_index[x]
        decrypted_message += odd_index_rev[x]
        x+=1
    else:
        decrypted_message += even_index[x]
        break

print(decrypted_message)
