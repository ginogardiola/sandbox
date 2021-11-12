# winning node combinations for Human and CPU

#   1 _ _   1 2 3   _ _ 3   _ _ _   _ _ _   _ 2 _   
#   _ 5 _   _ _ _   _ 5 _   4 5 6   _ _ _   _ 5 _   
#   _ _ 9   _ _ _   7 _ _   _ _ _   7 8 9   _ 8 _

from random import randrange

nodes = ['_','_','_','_','_','_','_','_','_','_']
counter = 2
w = -1
g = 0
while counter <= len(nodes):
    cpu = randrange(8)
    counter += 1
    for x in range(1,len(nodes)):
        if(x%3==0):
            print(nodes[x],end="\n")
        else:
            print(nodes[x],end=" ")
    human = input("\nenter a number ranging from 1 to 9: ")
    while nodes[int(cpu)] == "O":
        cpu = randrange(8)
        counter -= 1
    while nodes[int(cpu)] == "O":
        print("cpu trying another number..")
        cpu = randrange(8)
        
    nodes[int(cpu)] = "O"
    while int(human) > len(nodes):
        human = input("\nerror! enter only a number ranging from 1 to 9: ")
    while nodes[int(human)] == "X" or nodes[int(human)] == "O":
        for x in range(1,len(nodes)):
            if(x%3==0):
                print(nodes[x],end="\n")
            else:
                print(nodes[x],end=" ")
        human = input("\nerror! node is not empty. choose another node:  ")
        counter -= 1
    nodes[int(human)] = "X"
    if counter>= len(nodes):
        print(" draw! ")
        break

    #detect winning node combinations for player
    if nodes[1] == "X" and nodes[5] == "X" and nodes[9] == "X":break
    w = 1 
    if nodes[1] == "X" and nodes[2] == "X" and nodes[3] == "X":break
    w = 1 
    if nodes[3] == "X" and nodes[5] == "X" and nodes[7] == "X":break
    w = 1 
    if nodes[4] == "X" and nodes[5] == "X" and nodes[6] == "X":break
    w = 1 
    if nodes[7] == "X" and nodes[8] == "X" and nodes[9] == "X":break
    w = 1 
    if nodes[2] == "X" and nodes[5] == "X" and nodes[8] == "X":break
    w = 1

    #detect winning node combinations for cpu
    if nodes[1] == "O" and nodes[5] == "O" and nodes[9] == "O":break
    w = 0 
    if nodes[1] == "O" and nodes[2] == "O" and nodes[3] == "O":break
    w = 0 
    if nodes[3] == "O" and nodes[5] == "O" and nodes[7] == "O":break
    w = 0 
    if nodes[4] == "O" and nodes[5] == "O" and nodes[6] == "O":break
    w = 0 
    if nodes[7] == "O" and nodes[8] == "O" and nodes[9] == "O":break
    w = 0 
    if nodes[2] == "O" and nodes[5] == "O" and nodes[8] == "O":break
    w = 0 

if w==1:
    for x in range(1,len(nodes)):
        if(x%3==0):
            print(nodes[x],end="\n")
        else:
            print(nodes[x],end=" ")
    print("\n Tik Tak Toe! You win. \n")
else:
    for x in range(1,len(nodes)):
        if(x%3==0):
            print(nodes[x],end="\n")
        else:
            print(nodes[x],end=" ")
    print("\n Tik Tak Toe! You lose. \n")
    
    


