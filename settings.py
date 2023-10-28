import pygame
bg = pygame.image.load('images/bg.png')
bg2 = pygame.image.load('images/cyberpunk-street.png')
bullet = pygame.image.load('images/bullet.png')
BULLET = pygame.transform.scale(bullet, (30, 30))

is_jump = False
jump_counter = 10
BG_X = 0
K = 0
A = 0
Q = 0
PLAYER_X = 50
PLAYER_Y = 330
BAD_PLAYER_X = 1000
PLAYER_SPEED = 9
LIST_RIGHT = []
LIST_LEFT = []
LIST_STAY = []
LIST_WITH_BAD = []
BAG_PERSON = pygame.image.load('images/bad_person/photo_2023-10-26_23-43-23.jpg')
BAG_PERSON = pygame.transform.scale(BAG_PERSON, (70, 70))
list_go_right = [pygame.image.load('images/go_left/photo_2023-10-26_23-01-07.jpg'),
                 pygame.image.load('images/go_left/photo_2023-10-26_23-01-04.jpg')]
list_go_left = [pygame.image.load('images/go_right/photo_2023-10-26_23-00-55.jpg'),
                pygame.image.load('images/go_right/photo_2023-10-26_23-00-59.jpg')]
stay_on_place = [pygame.image.load('images/place/photo_2023-10-26_23-09-15.jpg'),
                 pygame.image.load('images/place/photo_2023-10-26_23-09-20.jpg')]

for i in list_go_right:
    i = pygame.transform.scale(i, (100, 100))
    LIST_RIGHT.append(i)

for i in list_go_left:
    i = pygame.transform.scale(i, (100, 100))
    LIST_LEFT.append(i)

for i in stay_on_place:
    i = pygame.transform.scale(i, (100, 100))
    LIST_STAY.append(i)


