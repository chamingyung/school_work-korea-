# env name : rand_arr

# the num of student : >=27 , <=30

import pygame 
import random
import openpyxl


# Initialization 

pygame.init()

# Setting Screen

screen_width = 900
screen_height = 600
screenSize = (screen_width, screen_height)
gameScreen = pygame.display.set_mode((screen_width,screen_height))

# Setting Title
pygame.display.set_caption("Random Seat Algorithm")

# Font
font = pygame.font.SysFont("arial", 32)
titleFont = pygame.font.SysFont("malgungothic", 32, True)
tableFont = pygame.font.SysFont("malgungothic", 22)
authorFont = pygame.font.SysFont("malgungothic", 18)

# Text
titleText = titleFont.render("좌석 배정 프로그램", True, (0,0,255))
tableText = tableFont.render("교탁", True, (0,0,0))
authorText = authorFont.render("종료 후 print.xlsx 열면 자리배치도 출력가능.   제작: chamingyung@outlook.com(차민경)", True, (0,155,0))

# Position
titlePosition = (screenSize[0] // 2 - titleText.get_width() // 2, 9) 
tablePosition = (screenSize[0]//2 - tableText.get_width()//2, 55)
authorPosition = (screenSize[0] // 2 - authorText.get_width() // 2 , screenSize[1] -50 ) 

# Setting student nums, position nums 
size = int(input("""
---------------------------------------------------------------------------
이 프로그램은 학급 좌석을 랜덤으로 배치하되, 두세 명의 학생의 간격을 떨어트리는 프로그램입니다. 
예를 들어, 한 학급에 학폭사건에 연루된 학생이 두세 명 있으면 떨어트릴 수 있습니다. 
---------------------------------------------------------------------------                 
학급 인원수를 입력하세요(27이상30이하)(예: 28) :"""))

numbers = list(range(1,size+1))  # 1 ~ size 
positions = []

# 1st Col
for i in range(5) : 
    for j in range(2) : 
        positions.append((100+j*100, 100+i*100))

# 2nd Col
for i in range(5) : 
    for j in range(2) : 
        positions.append((400+100*j, 100+i*100))


# 3rd Col
if size == 27 or size == 28 : 
    for i in range(4) :
        for j in range(2) :
            positions.append((700+100*j, 100+100*i))
elif size == 29 or size == 30 : 
    for i in range(5) : 
        for j in range(2) : 
            positions.append((700+100*j, 100+100*i))
    

# Selecting 3 students

mode = input ("""
---------------------------------------------------------------------------
떨어트리는 기능 없이 그냥 랜덤으로 돌리시려면 알파벳 n을, 
학생을 떨어트리려면 알파벳 y를 입력하세요 (y 또는 n) :  """)

if mode == 'n' : 
    print("""
          -------------------------------------------------------------------
        (중요!) 이제 학생들에게 이 명령창이 보이지 않도록, 이 명령창을 최소화하여 숨겨주세요. 
        랜덤배정기 화면에서 Enter 키를 누를 때마다 자리가 랜덤하게 섞입니다. 
        
        저작권 및 제작 문의 : http://cha8.ap-northeast-2.elasticbeanstalk.com/  
          chamingyung@outlook.com(차민경)
          ---------------------------------------------------------------------""")

elif mode == 'y' :
    sep = int(input("몇 명의 학생을 분리할까요(2 또는 3) : "))
    if sep == 2 : 
        a = int(input("첫 번째 학생의 번호는? (예: 24)  : "))
        b = int(input("두 번째 학생의 번호는? (예: 25)  : "))
    elif sep == 3 : 
        a = int(input("첫 번째 학생의 번호는? (예: 24)  : "))
        b = int(input("두 번째 학생의 번호는? (예: 25)  : "))
        c = int(input("세 번째 학생의 번호는? (예: 27)  : "))
    print("""
          ------------------------------------------------------------------------------------
          (중요!) 이제 학생들에게 이 명령창이 보이지 않도록, 이 명령창을 최소화하여 숨겨주세요. 
          랜덤배정기 화면에서 Enter 키를 누를 때마다 자리가 랜덤하게 섞입니다. 
          랜덤배정 후 프로그램 종료하시고 print.xlsx (엑셀파일) 여시면 자리배치도(교탁에서 보는 방향으로 정렬된 것)를 출력할 수 있습니다.

          저작권 및 제작 문의 : http://cha8.ap-northeast-2.elasticbeanstalk.com/  
          chamingyung@outlook.com(차민경)
          -----------------------------------------------------------------------------------
          """)


# LOOP
    
running = True
while running : 
    # Screen Color
    gameScreen.fill((255,255,255))

    # Dealing Events
    for event in pygame.event.get() : 
        # Terminating
        if event.type == pygame.QUIT : 
            running = False
        if event.type == pygame.KEYDOWN : 
            if mode == 'n' : 
                if event.key == pygame.K_RETURN : 
                    random.shuffle(numbers)
            elif mode == 'y' : 
                if sep == 2 : 
                    rest = [k for k in numbers if k not in [a,b]]
                    c_idx = random.randint(0,25)
                    c = rest[c_idx]
                else : pass
                if event.key == pygame.K_RETURN : 
                    # Shuffering nums except a, b, c
                    others = [ n for n in numbers if n not in (a,b,c)]
                    random.shuffle(others)
                    # Determinating a, b, c in 1st col or 3rd col
                    ring = [
                        [1, 13, 23], #1
                        [2, 13, 26], #2
                        [3, 15, 20], #3
                        [5, 10, 22], #4
                        [3, 6, 13], #5
                        [7, 12, 20], #6
                        [7, 15, 20], #7
                        [5, 15, 21], #8
                        [4, 12, 22], #9
                        [3, 15, 21], #10
                        [3, 16, 24], #11
                        [1, 11, 23], #12
                        [0, 15, 25], #13
                        [0, 17, 20], #14
                        [2, 7, 13], # 15
                        [1, 5, 15], # 16
                        [12, 20, 24], # 17
                        [10, 16, 25], # 18
                        [23, 10, 1], # 25, 11, 1  #19
                        [20, 13, 4], # 22, 14, 4  # 20
                        [18, 11, 2], # 20, 12, 2, # 21
                        [18, 14, 3], # 20, 15, 3  # 22
                        [22, 9, 5], #24, 10, 5 #23
                        [22, 10, 0], #24, 11, 0 #24
                        [20, 26, 5], #22, 17, 5  # 25
                        [19, 11, 0], #21, 12, 0  #26
                        [23, 3, 11], #25, 3, 11  #27
                        [14, 2, 10], #16, 2, 10  #28
                        [19, 3, 17], #21, 3, 17  #29
                        [21, 5, 13], #23, 5, 13  #30
                        [20, 2, 16], #22, 16, 2  #31
                        [13, 1, 4], #15, 1, 4  #32
                        [11, 3, 6], #13, 3, 6  #33
                        [9, 2, 7], #11, 2, 7   #34
                        [15, 4, 10], #17, 4, 10  #35
                        [17, 5, 11], #19, 5, 11  #36
                        [11,23,4], # 12, 24, 4   #37
                        [12, 24, 1], #13, 25, 1  #38
                        [13,21,0], #14, 22, 0  #39
                        [11,20,6], #12, 21, 6  #40
                        [9,19,2] #10, 20, 2  #41

                    ]
                    k = random.randint(0,40) 
                    # Calculating Index of a, b, c
                    index_a, index_b, index_c = ring[k][0], ring[k][1], ring[k][2]

                    # Inputting indexes of a,b,c into numbers list
                    numbers = others[:]
                    numbers.insert(index_a, a)
                    numbers.insert(index_b, b)
                    numbers.insert(index_c, c)

    # Showing title, author

    gameScreen.blit(titleText, titlePosition)
    gameScreen.blit(tableText, tablePosition)
    gameScreen.blit(authorText, authorPosition)

    # Matching nums and coordinates

    for i in range(size) : 
        number =numbers[i]
        position = positions[i]
        text = font.render(str(number), True, (0,0,0))
        gameScreen.blit(text, position)


    # Updating Screen
    pygame.display.flip()


# Terminating
pygame.quit()

# Writing xlsx File for Printing 

workbook = openpyxl.load_workbook('print.xlsx')

sheet = workbook['Sheet2']
for i, num in enumerate(numbers) : 
    sheet.cell(row=i+2, column = 5, value=num)
workbook.save('print.xlsx')
workbook.close()



