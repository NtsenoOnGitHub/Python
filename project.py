userWord = str(input('Enter a word to check: ').strip())
resultWord = ''
length = len(userWord) - 1

while length >= 0:
    resultWord += userWord[length]
    length -= 1

if userWord == resultWord:
    result = True
else:
    result = False

print(result)