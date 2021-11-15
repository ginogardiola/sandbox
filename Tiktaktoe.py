# winning node combinations for Human and CPU

#   1 _ _   1 2 3   _ _ 3   _ _ _   _ _ _   _ 2 _   1 _ _   _ _ 3
#   _ 5 _   _ _ _   _ 5 _   4 5 6   _ _ _   _ 5 _   4 _ _   _ _ 6
#   _ _ 9   _ _ _   7 _ _   _ _ _   7 8 9   _ 8 _   7 _ _   _ _ 9

node = ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_', ]

from random import randrange

c = 1
w = 0
while c < len(node):
    c += 1
    for x in range(1, len(node)):
        if x % 3 == 0:
            print(node[x], end="\n")
        else:
            print(node[x], end=" ")
    human = input("enter a number from 1 to 9: ")
    while node[int(human)] == "O" or node[int(human)] == "X":
        human = input("ERROR: node is already occupied. enter another number from 1 to 9: ")
    node[int(human)] = "O"
    cpu = randrange(1,9)
    while node[int(cpu)] == "X" or node[int(cpu)] == "O":
        cpu = randrange(1, 9)
    node[int(cpu)] = "X"
    # detect winning node combinations for human
    if node[1] == "O" and node[5] == "O" and node[9] == "O":break
    w = 1
    if node[1] == "O" and node[2] == "O" and node[3] == "O":break
    w = 1
    if node[3] == "O" and node[5] == "O" and node[7] == "O":break
    w = 1
    if node[4] == "O" and node[5] == "O" and node[6] == "O":break
    w = 1
    if node[7] == "O" and node[8] == "O" and node[9] == "O":break
    w = 1
    if node[2] == "O" and node[5] == "O" and node[8] == "O":break
    w = 1
    if node[3] == "O" and node[6] == "O" and node[9] == "O": break
    w = 1
    # detect winning node combinations for CPU
    if node[1] == "X" and node[5] == "X" and node[9] == "X":break
    w = 0
    if node[1] == "X" and node[2] == "X" and node[3] == "X":break
    w = 0
    if node[3] == "X" and node[5] == "X" and node[7] == "X":break
    w = 0
    if node[4] == "X" and node[5] == "X" and node[6] == "X":break
    w = 0
    if node[7] == "X" and node[8] == "X" and node[9] == "X":break
    w = 0
    if node[2] == "X" and node[5] == "X" and node[8] == "X":break
    w = 0
    if node[3] == "X" and node[6] == "X" and node[9] == "X": break
    w = 0
for x in range(1, len(node)):
    if x % 3 == 0:
        print(node[x], end="\n")
    else:
        print(node[x], end=" ")
if w == 1:
    print("Tic-Tac-Toe! YOU WIN.")
elif w == 0:
    print("Tic-Tac-Toe! YOU LOSE.")
else:
    print("DRAW! no one wins.")