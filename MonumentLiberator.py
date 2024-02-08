symbols = ',\t;:|(){}[]'
with open("01_monuments.txt", "r") as file: #needs a text file
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

partsToClean = 0
for element in ['build_trigger', 'can_use_modifiers_trigger', 'can_upgrade_trigger', 'conditional_modifier']: # Count how many parts needs to be cleaned
    partsToClean += words.count(element)
print(partsToClean)
for part in range(partsToClean):
    indices = [index for (index, value) in enumerate(words) if value == 'build_trigger' or value == 'can_use_modifiers_trigger' or value == 'can_upgrade_trigger' or value == 'conditional_modifier']
    triggerIndex = indices[part]
    tempIndex = triggerIndex
    tabCount = 0
    currentTabCount = 0

    while words[triggerIndex - tabCount - 1] == '\t': # Count the number of tabs before the trigger
        tabCount += 1

    while True: # Finds the index of the target closing brace
        tempIndex += 1
        if words[tempIndex] == '}':
            while words[tempIndex - currentTabCount - 1] == '\t':
                currentTabCount += 1
            if tabCount == currentTabCount:
                braceIndex = tempIndex
                break
            else:
                currentTabCount = 0

    for j in range(braceIndex - 1, triggerIndex + 4, -1):
        words.pop(j)

with open("usableMonuments.txt", "w") as file:
    for i in range(len(words)):
        file.write(words[i])
