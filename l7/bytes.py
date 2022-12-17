characters = b"\x63\x6c\x69\x63\x68\xe9"
print(characters)
print(characters.decode('latin-1'))

word = "cliché"
print(word.encode('UTF-8'))
print(word.encode('Latin-1'))
print(word.encode('CP437'))
# print(word.encode('ascii'))
