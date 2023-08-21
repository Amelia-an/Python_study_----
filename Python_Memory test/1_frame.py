import pygame

#초기화
pygame.init()
screen_width = 1280 #가로표기
screen_height = 720 #세로크기
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Memory Game")

#게임 루프
running = True #게임이 실행중인가
while running:
    #이벤트 루프
    for evnet in pygame.event.get(): #어떤 이벤트 발생했냐
        if evnet.type == pygame.QUIT: #창이 닫히는 이벤트냐
            running = False # 게임이 더 이상 실행중이 아니다
            
#게임 종료
pygame.quit()
