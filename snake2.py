import random
snake = [[0, 0]]
boardSize = [21, 6]
apple = [2, 0]
highScore = 0

def show_board(snake, apple):
    boardText = ""
    for i in range(boardSize[1]):
        for i in range(boardSize[0]):
            boardText += "-"
        boardText += "\n"

    boardText = list(boardText)
    
    boardText[apple[0] + apple[1] * (boardSize[0] + 1)] = "a"
    for segment in snake:
        boardText[segment[0] + segment[1] * (boardSize[0] + 1)] = "S"

    head = snake[0]
    boardText[head[0] + head[1] * (boardSize[0] + 1)] = "H"

    boardText = "".join(boardText)
    boardText = boardText[:-1]
    print(boardText)

def lose():
    global highScore
    print()
    print()
    print("You Lose!")
    print("Game Over")
    print("Score: " + str(len(snake)))
    if len(snake) > highScore: # files don't seem to actually work on my calculator
        try:
            highScore = len(snake)
            file = open("score.txt", "w")
            file.write(str(highScore))
            file.close()
            print()
            print("New High Score!")
        except:
            pass



try:
    file = open("score.txt", "r")
    highScore = int(file.read)
    file.close()
except:
    pass

print("Welcome to SNAKE!")
print()
print("High Score: " + str(highScore))
print()
input("press EXE ")
print()
print()
print("Controls:")
print()
print("Movement:")
print("8,6,2, and 4")
print()
print("press exe between frames")
input()

topography = None
while topography == None:
    print("""
Choose a topography:
 1. Square (boring)
 2. Torus
 3. Mobius Strip
 4. Sphere
 5. Klein Bottle""")
    try:
        topography = int(input())
        if topography > 5 or topography < 1:
            topography = None
    except: pass


direction = ""
while True:
    show_board(snake, apple)
    move = input().upper()

    if (move == "6" or move == "R") and direction != "L":
        direction = "R"
    if (move == "4" or move == "L") and direction != "R":
        direction = "L"
    if (move == "8" or move == "U") and direction != "D":
        direction = "U"
    if (move == "2" or move == "D") and direction != "U":
        direction = "D"
        
    
    
    head = snake[0].copy()
    if direction == "R":
        head[0] += 1
    if direction == "L":
        head[0] -= 1
    if direction == "U":
        head[1] -= 1
    if direction == "D":
        head[1] += 1


    if direction != "":
        if head[0] < 0:
            if topography == 1 or topography == 3:
                lose()
                break
            head[0] += boardSize[0]
            if topography == 4:
                print("test 1")
                head[1] = boardSize[1] - head[1] - 1
        
        if head[0] >= boardSize[0]:
            if topography == 1 or topography == 3:
                lose()
                break
            head[0] -= boardSize[0]
            if topography == 4:
                print("test 2", head)
                head[1] = boardSize[1] - head[1] - 1
        
        if head[1] < 0:
            if topography == 1:
                lose()
                break
            head[1] += boardSize[1]
            if topography == 3 or topography == 4 or topography == 5:
                print("test 3")
                head[0] = boardSize[0] - head[0] - 1
        
        if head[1] >= boardSize[1]:
            if topography == 1:
                lose()
                break
            head[1] -= boardSize[1]
            if topography == 3 or topography == 4 or topography == 5:
                print("test 4", head)
                head[0] = boardSize[0] - head[0] - 1
        
        if head in snake:
            lose()
            break
        
        if head == apple:
            snake.append([0, 0])
            while apple in snake or apple == head:
                apple = [random.randint(0, boardSize[0]-1), random.randint(0, boardSize[1]-1)]
        
        for i in range(len(snake)-1, 0, -1):
            snake[i] = snake[i-1]
        
        snake[0] = head
    
