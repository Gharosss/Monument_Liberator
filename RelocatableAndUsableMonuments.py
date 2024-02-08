symbols = ',\t;:|(){}[]'
with open("usableMonuments.txt", "r") as file: #needs a text file
    text = file.read()

words = []
word = ''
for i in range(len(text)):
    if text[i] == ' ':
        if word != '':
            words.append(word)
            word = ''
        words.append(' ')
    else:
        if not text[i] in symbols:
            word = word + text[i]
        elif word != '':
            words.append(word)
            word = text[i]
            words.append(word)
            word = ''
        else:
            word = text[i]
            words.append(word)
            word = ''


indices = [index for (index, value) in enumerate(words) if value == 'can_be_moved']
for j in range(len(indices)):
    words[indices[j]+4] = 'yes\n'

with open("relocatableMonuments.txt", "w") as file:
    for i in range(len(words)):
        file.write(words[i])
