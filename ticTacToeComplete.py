TABELA_TODA = list('123456789') #lista com todas as posições da tabela do jogo da velha
X, O, VAZIO = 'X', 'O', ' ' # As marcações para preencher os vazios da tabela do jogo da velha

def main():
    while True:
        print('Bem vindo ao Jogo da Velha!')
        jogo = novoJogoDaVelha()


        jogadorAtual, proximoJogador = X, O

        while True:
            print(imprimeJogoDaVelha(jogo))

            move = None
            while not temEspacoValido(jogo, move):
                print(f'Qual é a posição que o jogador {jogadorAtual} deseja preencher?')
                move = input()
            
            atualizaJogo(jogo, move, jogadorAtual)

            if teveGanhador(jogo, jogadorAtual):
                print(imprimeJogoDaVelha(jogo))
                print(f'Jogador {jogadorAtual} ganhou!')
                break
            elif tabelaCheia(jogo):
                print(imprimeJogoDaVelha(jogo))
                print('Empate!')
                break

            jogadorAtual, proximoJogador = proximoJogador, jogadorAtual

        continuaJogo = str(input('Deseja jogar um novo Jogo da Velha? ("Sim", "Não") ')).lower().split()

        if 's' in continuaJogo:
            continue
        else:
            break
        
        print('Obrigado por jogar!')
        

def novoJogoDaVelha():
    board = {}
    for space in TABELA_TODA:
        board[space] = VAZIO
    return board

def imprimeJogoDaVelha(board):
    return '''
      {}|{}|{}  1 2 3
      -+-+-
      {}|{}|{}  4 5 6
      -+-+-
      {}|{}|{}  7 8 9'''.format(board['1'], board['2'], board['3'], board['4'], board['5'], board['6'], board['7'], board['8'], board['9'])

def temEspacoValido(board, space):
    return space in TABELA_TODA and board[space] == VAZIO

def atualizaJogo(board, lugar, simbolo):
    board[lugar] = simbolo

def teveGanhador(board, jogador):
    b, player = board, jogador

    return ((b['1'] == b['2'] == b['3'] == player) or 
            (b['4'] == b['5'] == b['6'] == player) or
            (b['7'] == b['8'] == b['9'] == player) or
            (b['1'] == b['4'] == b['7'] == player) or
            (b['2'] == b['5'] == b['8'] == player) or
            (b['3'] == b['6'] == b['9'] == player) or
            (b['3'] == b['5'] == b['7'] == player) or
            (b['1'] == b['5'] == b['9'] == player)) 

def tabelaCheia(board):
    for space in TABELA_TODA:
        if board[space] == VAZIO:
            return False
    return True

if __name__ == '__main__':
    main()