#! python3
# fixeTheBug.py - Achar o bug e corrigir o programa.

# Script que está no livro:
import random

guess = ''

while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()

# toss = random.randint(0,1) # 0 é coroa (tails), 1 é cara (heads)
coin = ['heads', 'tails'] # Minha correção
toss = random.choice(coin) # Minha correção
if toss == guess:
    print('You got it!')
else:
    print('Nope! Guess again!')
    guess = input()
    if toss == guess:
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')


# Minha descoberta
# No programa original -> if toss == guess deu um bug pois, toss é um número inteiro (0 ou 1) e guess é string ('heads' ou 'tails')
# Com isso, como eles não são iguais, irá para else, mesmo que você acertou o palpite.

# Minha solução
# Criei uma lista salvo na variavel 'coin' e utilizei uma outra função do random (em vez de radint, usei choice) para escolher
# o que está na lista e assim torna-los compatível com mesmo tipo de dados.