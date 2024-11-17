import random

winComb = [[0,1,2],[0,4,8],[0,3,6],[1,4,7],[2,4,6],[2,5,8],[3,4,5],[6,7,8]]
userChar = 'X'
compChar = 'O'
spaceChar = ' '

def getFirstTurn():
    choice = input('Do you want to go first? Enter Y/y if you want to go first: ')
    if choice in ['Y', 'y']:
        print('User will start first')
        return userChar
    else:
        print('Computer will start first')
        return compChar
    
def startTicTacToe():
    return [spaceChar for i in range(9)]

def printTicTacToe(ticTacToe):
    print(ticTacToe[0], '|', ticTacToe[1], '|', ticTacToe[2], sep='')
    print('-|-|-')
    print(ticTacToe[3], '|', ticTacToe[4], '|', ticTacToe[5], sep='')
    print('-|-|-')
    print(ticTacToe[6], '|', ticTacToe[7], '|', ticTacToe[8], sep='')
    print('\n')
    
def enterNextPos(ticTacToe):
    availablePositions = [(i + 1) for i in range(9) if ticTacToe[i] == spaceChar]
    while True:
        pos = input('Choose among the available position ' + str(availablePositions) + ': ')
        pos = int(pos)
        if pos in availablePositions:
            break
        else:
            print('Wrong position choosen.')
    ticTacToe[pos - 1] = userChar
    return ticTacToe

def getAllPos(ticTacToe, char):
    allPos = [i for i in range(9) if ticTacToe[i] == char]
    return allPos

def reqPosForWin(ticTacToe, char):
    allPos = getAllPos(ticTacToe, char)
    for comb in winComb:
        reqComb = []
        for pos in comb:            
            if ticTacToe[pos] not in [char, spaceChar]:
                reqComb = []
                break
            elif (pos not in allPos) and (ticTacToe[pos] == spaceChar):
                reqComb.append(pos)
        
        if len(reqComb) == 1:
            break 
    return reqComb

def compPosEnter(ticTacToe):
    oCombAvail = reqPosForWin(ticTacToe, compChar)
    xCombAvail = reqPosForWin(ticTacToe, userChar)
    spaceCombAvail = getAllPos(ticTacToe, spaceChar)
    
    choosenPos = ''
        
    if len(oCombAvail) == 1:
        choosenPos = oCombAvail[0]
    elif len(xCombAvail) == 1:
        choosenPos = xCombAvail[0]
    elif ticTacToe[4] == spaceChar:
        choosenPos = 4
    elif ticTacToe[4] == compChar:
        if ticTacToe[1] == spaceChar:
            choosenPos = 1
        elif ticTacToe[3] == spaceChar:
            choosenPos = 3
        elif ticTacToe[5] == spaceChar:
            choosenPos = 5
        elif ticTacToe[7] == spaceChar:
            choosenPos = 7
    else:
        if ticTacToe[0] == spaceChar:
            choosenPos = 0
        elif ticTacToe[2] == spaceChar:
            choosenPos = 2
        elif ticTacToe[6] == spaceChar:
            choosenPos = 6
        elif ticTacToe[8] == spaceChar:
            choosenPos = 8
        else:
            choosenPos = random.choice(spaceCombAvail)
    print('Computer chooses position', choosenPos + 1, '\n')
    ticTacToe[choosenPos] = compChar 
    return ticTacToe
            
def checkWinner(ticTacToe):
    winner = None
    for comb in winComb:      
        if ticTacToe[comb[0]] == ticTacToe[comb[1]] == ticTacToe[comb[2]]:
            if spaceChar == ticTacToe[comb[0]]:
                continue
            elif compChar == ticTacToe[comb[0]] or userChar == ticTacToe[comb[0]]:
                winner = ticTacToe[comb[0]]
                break
        
    return winner

def ticTacToe():
    turn = getFirstTurn()
    ticTacToe = startTicTacToe()
    totalTurn = 0
    while True:
        printTicTacToe(ticTacToe)
        if turn == userChar:
            ticTacToe = enterNextPos(ticTacToe)
            turn = compChar
        else:
            ticTacToe = compPosEnter(ticTacToe)
            turn = userChar
        totalTurn = totalTurn + 1
        if totalTurn > 4:
            print('Winner Check')
            winner = checkWinner(ticTacToe)
            if winner in [userChar, compChar] or spaceChar not in ticTacToe:
                break
        
    if winner == userChar:
        print('You are the Winner!')
    elif winner == compChar:
        print('You are the Loser!')
    else:
        print('It is a tie!')        
    printTicTacToe(ticTacToe)

#Calling main function
ticTacToe()