import pygame

#시작 화면 보여주기
def display_start_screen():
    pygame.draw.circle(screen, WHITE, start_button.center, 60, 5)
    #흰색으로 동그라미를 그리는데 중심좌표는 start_button의 중심 좌표를 따라가고,
    #반지름은 60, 선 두께는 5
 
def display_game_screen():
    print("Game Start") 
 
 
#pos(position)에 해당하는 버튼 확인 
def check_buttons(pos):
    global start
    if start_button.collidepoint(pos):
        start = True
        
    
#초기화
pygame.init()
screen_width = 1280 #가로표기
screen_height = 720 #세로크기
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Memory Game")

#시작 버튼
start_button = pygame.Rect(0, 0, 120, 120) #버튼 크기 설정(왼,위,가로,세로)
start_button.center = (120, screen_height - 120)

#색깔
BLACK = (0,0, 0) #RGB -> 인터넷에 검색해보면 각 색깔 고유의 RGB 숫자를 알 수 있음
WHITE = (255, 255, 255)

#게임 시작 여부
start = False

#게임 루프
running = True #게임이 실행중인가
while running:
    click_pos = None 
    
    #이벤트 루프
    for evnet in pygame.event.get(): #어떤 이벤트 발생했냐
        if evnet.type == pygame.QUIT: #창이 닫히는 이벤트냐
            running = False # 게임이 더 이상 실행중이 아니다
        elif evnet.type == pygame.MOUSEBUTTONUP: #사용자가 마우스를 클릭했을 때
            click_pos = pygame.mouse.get_pos()
            print(click_pos)
            
            
    #화면 전체를 까맣게 칠함
    screen.fill(BLACK)        
    
    if start: 
        display_game_screen() #게임 화면 표기
    else:
        display_start_screen() #시작 화면 표시
        
    #사용자가 클릭한 좌표값이 있다면(어딘가 클릭을 했다면)    
    if click_pos:
        check_buttons(click_pos)
        
    
    #화면 업데이트
    pygame.display.update()
            
            
#게임 종료
pygame.quit()