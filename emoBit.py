#emoBit form ctf top 2024

# Mapping of emojis to binary values
emoji_to_binary = {
    '😸': '0',
    '😺': '1',
    ' ' : ' '
}

# The input string of emojis
file_object = open('emoBit.txt', encoding='utf8')
emoji_string = file_object.read()
file_object.close()

# Decode the string
binary_string = ''.join(emoji_to_binary[emoji] for emoji in emoji_string if emoji in emoji_to_binary)

print("Binary String:", binary_string)

#cyberchef use from binary
#after decode form binary you got the emoji
#use base100 for decode emoji
#last you the flag