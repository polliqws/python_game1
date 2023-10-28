import pygame
import sys
from settings import *

pygame.init()
screen = pygame.display.set_mode((900, 473), pygame.RESIZABLE)
clock = pygame.time.Clock()
TIMER = pygame.USEREVENT + 1
pygame.time.set_timer(TIMER, 3000)
playgame = True
is_jump = False
list_with_bullets = []
font = pygame.font.Font('images/font.ttf', 100)
text = font.render('You lose', False, 'Red')
restart = font.render('RESTART', True, 'Gray')
A = 0
jump_counter = 10
Q = 0
while True:
    if playgame:
        screen.blit(bg, (BG_X,0))
        screen.blit(bg, (900+BG_X, 0))
        if BG_X == -900:
            BG_X= 0
        BG_X -=1
        if K == 2:
            K = 0
        screen.blit(LIST_STAY[K], (PLAYER_X, PLAYER_Y))
        K+=1
        BAD_PLAYER_X -= 3
        PLAYER_X_RECT_RIGHT = LIST_RIGHT[0].get_rect(topleft=(PLAYER_X, PLAYER_Y))
        BAD_PLAYER_RECT = BAG_PERSON.get_rect(topleft=(BAD_PLAYER_X, 360))
        if list_with_bullets:
            for (i, el) in enumerate(list_with_bullets):

                screen.blit(BULLET, el)
                el.x +=10
            if LIST_WITH_BAD:
                for (q, item) in enumerate(LIST_WITH_BAD):
                    if el.colliderect(item):
                        LIST_WITH_BAD.pop(q)
                        list_with_bullets.pop(i)




        if LIST_WITH_BAD:
            for (el, i) in enumerate(LIST_WITH_BAD):
                screen.blit(BAG_PERSON, i)
                i.x-=10
                if i.x < -1:
                    LIST_WITH_BAD.pop(el)

                if PLAYER_X_RECT_RIGHT.colliderect(i):
                    playgame = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            screen.blit(LIST_LEFT[A], (PLAYER_X, PLAYER_Y))
            A+=1
            if A == 2:
                A = 0
            PLAYER_X-=PLAYER_SPEED
        if keys[pygame.K_d]:
            screen.blit(LIST_RIGHT[Q], (PLAYER_X, PLAYER_Y))
            Q += 1
            if Q == 2:
                Q = 0
            PLAYER_X += PLAYER_SPEED
        if not is_jump:
            if keys[pygame.K_SPACE]:
                is_jump = True
        else:
            if jump_counter >= -10:
                if jump_counter > 0:
                    PLAYER_Y -= (jump_counter ** 2) / 2
                else:
                    PLAYER_Y += (jump_counter ** 2) / 2
                jump_counter -= 1
            else:
                is_jump = False
                jump_counter = 10
    else:
        screen.fill((40, 33, 102))
        screen.blit(text, (100, 40))
        screen.blit(restart, (100, 200))

        x = pygame.mouse.get_pos()
        if restart.get_rect(topleft=(100, 100)).collidepoint(x) and pygame.mouse.get_pressed()[0]:
            playgame = True
            LIST_WITH_BAD.clear()
            PLAYER_X = 50


    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == TIMER:
            LIST_WITH_BAD.append(BAG_PERSON.get_rect(topleft=(1000, 360)))
        if event.type == pygame.KEYUP and event.key == pygame.K_q:
            list_with_bullets.append(BULLET.get_rect(topleft=(PLAYER_X+20, PLAYER_Y+30)))
    clock.tick(20)