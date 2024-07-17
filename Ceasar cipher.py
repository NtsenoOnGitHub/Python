textToEncrypt = input("Enter the message to encrypt: ").strip()
keyTodecrypt = int(input("Enter a key to decrypt the messgae: "))

alphabets = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

# attack

def _encrypter(text, key):
    textToReturn = ""
    counter = 0
    encryptedText = []
    for x in text:
        counter = 0
        if x != " ":
            for y in alphabets:
                if y == x and x != "z":
                    encryptedText.append(alphabets[counter + key])
                counter += 1
        else:
            encryptedText.append(" ")

    for x in encryptedText:
        textToReturn += "" + x
        
    return textToReturn

print(_encrypter(textToEncrypt, keyTodecrypt))

        