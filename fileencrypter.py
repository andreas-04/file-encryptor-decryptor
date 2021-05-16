count = 0
key = 5
#the key
decrypted = b'abcdefghijklmnopqrstuvwxyz1234567890 '
encrypted = b'qwertyuioplkjhgfdsazxcvbnm8490731625%'


scrambled = bytes.maketrans(decrypted, encrypted)
unscrambled = bytes.maketrans(encrypted, decrypted) 
#encrpt/decrypt functions
def encrypt(text):
    encryptedpass = text.translate(scrambled)
    return(encryptedpass)
def decrypt(text):
    ezpass = text.translate(unscrambled)
    return(ezpass)

#determines the file name/location
print('> Enter filename and path here')
usrfile = input("> ")

#determines the users choice for the program 
print('''
> enter a 1 to encrypt
> enter a 2 to decrypt
> enter a 0 to quit
''')
usrchoice = input('> ')
#encryption
if usrchoice == '1':
    while count != key:
        count += 1
        uf = open(usrfile , "r+")
        contentvar = uf.read()
    #opens a new variable to store the opened file in

    #erases original text
        uf.truncate(0)
    #writes the encrypted version to the file
        uf.write(encrypt(contentvar))
    print('> done, file hase been encrypted.')
#decryption
elif usrchoice == '2':
    while count != key:
        count += 1
        filecontent = open(usrfile , 'r+')
        contentvar = filecontent.read()
        uf = open(usrfile , "r+")
        uf.truncate(0)
        uf.write(decrypt(contentvar))
    print('> done, file has been decrypted')
elif usrchoice == '0':
    print(' ')
        
else:
    print('> improper answer')
        