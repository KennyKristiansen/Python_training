turn = 'X'
board = {'TL':' ','TM':' ','TR':' ',
         'ML':' ','MM':' ','MR':' ',
         'BL':' ','BM':' ','BR':' ',}
def printboard(board):
    print(board['TL'] + '|' + board['TM'] + '|' + board['TR'])
    print('-+-+-')
    print(board['ML'] + '|' + board['MM'] + '|' + board['MR'])
    print('-+-+-')
    print(board['BL'] + '|' + board['BM'] + '|' + board['BR'])

while turn != '':
    move = ''
    turn ='X'
    liste = list(board)
    printboard(board)
    print('Player ' + str(turn) +' will start.' )
    for i in range(0,9):
        print('Make your move, player ' + str(turn))
        move = input()
        if move in board:
            move_legal = board.get(move,False)
            if move_legal == ' ':
                board[move] = turn
            if move_legal == 'X':
                if i < 6:
                    print('Move not allowed')
                    continue
                else:
                    board[move] = turn
            if move_legal == 'O':
                if i < 6:
                    print('Move not allowed')
                    continue
                else:
                    board[move] = turn
        else:
            continue

        printboard(board)
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'
    print('Game has ended.')
