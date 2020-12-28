import os
from time import sleep

def check_winner(simbol):
    for i in winner:
        if board[i[0]] == simbol and board[i[1]] == simbol and board[i[2]] == simbol:
            print(f"{simbol} WON!!")
            return True
        else:
            if '' not in board:
                print("Gave Old!")
                return True


game = False
board = ['', '', '', '', '', '', '', '', '']
simbols = ['X', 'O']
winner = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6],
]
x = 0

while game != True:
    print(f"{'HASH':^18}")
    print("=" * 18)
    print(f"{board[0]:^5}|{board[1]:^5}|{board[2]:^5}")
    print("=" * 18)
    print(f"{board[3]:^5}|{board[4]:^5}|{board[5]:^5}")
    print("=" * 18)
    print(f"{board[6]:^5}|{board[7]:^5}|{board[8]:^5}")
    print("=" * 18)
    position = int(input("Position? ")) - 1
    simbol = x % 2
    if board[position] == '':
        board[position] = simbols[simbol]
        x += 1
    os.system('cls' if os.name == 'nt' else 'clear')
    game = check_winner(simbols[simbol])
print("Thanks For Playing")
print("-" * 18)
print(f"{'HASH':^18}")
print("-" * 18)
print(f"{board[0]:^5}|{board[1]:^5}|{board[2]:^5}")
print("-" * 18)
print(f"{board[3]:^5}|{board[4]:^5}|{board[5]:^5}")
print("-" * 18)
print(f"{board[6]:^5}|{board[7]:^5}|{board[8]:^5}")
print("-" * 18)
    
