import random
import sys

def check(box,name):
    if boxes[0][0] == boxes[0][1] == boxes[0][2]:
        print("Congrats " + name + " won!!!")
        sys.exit()
    elif boxes[1][0] == boxes[1][1] == boxes[1][2]:
        print("Congrats " + name + " won!!!")
        sys.exit()
    elif boxes[2][0] == boxes[2][1] == boxes[2][2]:
        print("Congrats " + name + " won!!!")
        sys.exit()
    elif boxes[0][0] == boxes[1][0] == boxes[2][0]:
        print("Congrats " + name + " won!!!")
        sys.exit()
    elif boxes[0][1] == boxes[1][1] == boxes[2][1]:
        print("Congrats " + name + " won!!!")
        sys.exit()
    elif boxes[0][2] == boxes[1][2] == boxes[2][2]:
        print("Congrats " + name + " won!!!")
        sys.exit()
    elif boxes[0][0] == boxes[1][1] == boxes[2][2]:
        print("Congrats " + name + " won!!!")
        sys.exit()
    elif boxes[0][2] == boxes[1][1] == boxes[2][0]:
        print("Congrats " + name + " won!!!")
        sys.exit()
    else:
        return 0



print("""
Welcome to Tic Tac Toe
Start by telling us your name
"""
    )

member_1 = input("Player 1: ")
member_2 = input("Player 2: ")
members = [member_1, member_2]

player_1 = random.choice(members)
player_2 = ''
if player_1 == member_1:
    player_2 = member_2
else:
    player_2 = member_1

print("We have randomly chosen the first player to be:  " + player_1)

print("This is the playing grid. Do input the values of the box you want to choose")
print("In the format (top number) + (bottom number)")
boxes = [
    [11, 12, 13],
    [21, 22, 23],
    [31, 32, 33]
]

print("""

     1  2  3
   +--------+
1  |  |  |  | 
   +--------+
2  |  |  |  |
   +--------+
3  |  |  |  |
   +--------+ 
""")

round_what = 1

for round_what in range(1,11):
    if (round_what%2) != 0 and round_what<5:
        choice = int(input(player_1+ " : "))
        x = 0
        y = 0

        for x in range(0, 3):
            for y in range(0, 3):
                if choice == boxes[x][y]:
                    boxes[x][y] = "\U0001F47B"
                    print(" ".join(map(str, boxes[0])))
                    print(" ".join(map(str, boxes[1])))
                    print(" ".join(map(str, boxes[2])))
                    break
                else:
                    y += 1
            x += 1
    elif (round_what%2) != 0 and 4 < round_what<10:
        choice = int(input(player_1+ " : "))
        x = 0
        y = 0

        for x in range(0, 3):
            for y in range(0, 3):
                if choice == boxes[x][y]:
                    boxes[x][y] = "\U0001F47B"
                    print(" ".join(map(str, boxes[0])))
                    print(" ".join(map(str, boxes[1])))
                    print(" ".join(map(str, boxes[2])))
                    check_win = check(boxes, player_1)
                    break
                else:
                    y += 1
            x += 1
    elif (round_what%2) ==0 and round_what<6:
        choice = int(input(player_2 +" : "))
        x = 0
        y = 0

        for x in range(0, 3):
            for y in range(0, 3):
                if choice == boxes[x][y]:
                    boxes[x][y] = "\U0001F47D"
                    print(" ".join(map(str, boxes[0])))
                    print(" ".join(map(str, boxes[1])))
                    print(" ".join(map(str, boxes[2])))
                    break
                else:
                    y += 1
            x += 1
    elif (round_what % 2) == 0 and 5 < round_what < 10:
        choice = int(input(player_2 +" : "))
        x = 0
        y = 0

        for x in range(0, 3):
            for y in range(0, 3):
                if choice == boxes[x][y]:
                    boxes[x][y] = "\U0001F47D"
                    print(" ".join(map(str, boxes[0])))
                    print(" ".join(map(str, boxes[1])))
                    print(" ".join(map(str, boxes[2])))
                    check_win = check(boxes, player_2)
                    break
                else:
                    y += 1
            x += 1
    elif round_what == 10:
        print("Its a draw no one won!")
        sys.exit()
    round_what += 1








