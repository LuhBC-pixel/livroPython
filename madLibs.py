with open('phrase.txt') as arquivo:
    print(arquivo.read())
    
adjective = str(input('Enter an adjective:\n'))
noun = str(input('Enter a noun:\n'))
verb = str(input('Enter a verb:\n'))
noun1 = str(input('Enter a noun:\n'))

print(f'The {adjective} panda walked to the {noun} and then {verb}. A nearby {noun1} was unaffected by these events.')

with open('phrase1.txt', 'w') as arquivo:
    arquivo.write(f'The {adjective} panda walked to the {noun} and then {verb}. A nearby {noun1} was unaffected by these events.')