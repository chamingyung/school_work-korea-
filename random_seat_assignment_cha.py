import pygame

import random

# Initialization
pygame.init()

# Setting Screen

screen_width = 900
screen_height = 600
screenSize = (screen_width, screen_height)
gameScreen = pygame.display.set_mode((screen_width, screen_height))

# Setting Title
pygame.display.set_caption("Random Seat Assignment Algorithm")

# Font
font = pygame.font.SysFont("arial", 32)
titleFont = pygame.font.SysFont("malgungothic", 32, True)
authorFont = pygame.font.SysFont("malgungothic", 20)

# Text
titleText = titleFont.render("좌석 배정 프로그램", True, (0,0,255))
authorText = authorFont.render("학급 인원 수에 맞게 제작 문의 : 차민경(chamingyung@outlook.com)", True, (0,155,0))

# Position
titlePosition = (screenSize[0] // 2 - titleText.get_width() // 2, 20)
authorPosition = (screenSize[0] // 2 - authorText.get_width() // 2, screenSize[1] - 50)
# Setting student nums, position nums
numbers = list(range(1,29))
positions = []

# 1st Column
for i in range(5) :
    for j in range(2) :
        positions.append((100+j*100, 100+i*100))

# 2nd Column
for i in range(5) :
    for j in range(2) :
        positions.append((400+j*100, 100+i*100))

# 3rd Column
for i in range(4) :
    for j in range(2) :
        positions.append((700+j*100, 100+i*100))

# Selecting 2 students
mode = input("""
이 프로그램은 학급 좌석을 랜덤으로 배치하되 피치 못하게 자리를 떨어트려 놓아야 하는 학생 두 명만 좌석을 떨어트려 주는 프로그램입니다. 
단순 말썽 등에 적용하는 것은 삼가주시고 학폭과 같이 위험성이 있어 떨어트려야 하는 경우에만 사용해 주세요. 
떨어트리는 기능 없이 그냥 랜덤으로 돌리시려면 알파벳 n을,
두 학생의 번호를 지정하여 떨어트리려면 알파벳 y를 입력해 주세요 : """)
if mode == 'y' :
    a = int(input("첫번째 학생의 번호를 적어주세요 (예 : 12) : "))
    b = int(input("두 번째 학생의 번호를 적어주세요 (예 : 25) : "))
    print("""이제 이 글자가 학생들에게 보이지 않도록 이 창은 크기를 최소화하여 숨겨 주세요. 
    랜덤배정기 화면에서 Enter 키를 누를 때마다 자리가 랜덤하게 섞입니다. """)

# LOOP
running = True
while running :
    # Screen Color
    gameScreen.fill((255,255,255))

    # Dealing Events
    for event in pygame.event.get():
        # Terminating
        if event.type == pygame.QUIT :
            running = False
        if event.type == pygame.KEYDOWN :
            if mode == 'n' :
                if event.key == pygame.K_RETURN:
                    random.shuffle(numbers)

            elif mode == 'y' :
                if event.key == pygame.K_RETURN :
                    # Shuffling nums except a,b
                    others = [n for n in numbers if n not in (a,b)]
                    random.shuffle(others)
                    # Determining a,b in 1st col or 3rd col
                    col_a = random.choice([0,2])
                    col_b = 2 - col_a   # WOW......
                    row_a = random.randint(0,4)                  # ?
                    row_b = random.randint(0,3)
                    # Calculating Index of a and b
                    index_a = col_a * 10 + row_a * 2
                    index_b = col_b * 10 + row_b * 2
                    # Inputting indexes of a and b into numbers list
                    numbers = others[:]
                    numbers.insert(index_a, a)
                    numbers.insert(index_b, b)




    # Showing title, author

    gameScreen.blit(titleText, titlePosition)
    gameScreen.blit(authorText, authorPosition)

    # Matching nums and coordinates

    for i in range(28) :
        number = numbers[i]
        position = positions[i]
        text = font.render(str(number), True, (0,0,0))
        gameScreen.blit(text, position)

        print(i, number, position)



    # Renewing Screen
    pygame.display.flip()

# Terminnating
pygame.quit()



