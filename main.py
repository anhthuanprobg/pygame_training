import pygame

from game_object import GameObject, add, update, render
from enemy import Enemy
from bullet import PlayerBullet
from player import Player
from input_manager import InputManager

clock = pygame.time.Clock()
pygame.init()
SCREEN_SIZE = (400, 600)
canvas = pygame.display.set_mode(SCREEN_SIZE)

pygame.display.set_caption("Micro-war")


input_manager = InputManager()
player = Player(200, 540, input_manager)
player.image = pygame.image.load("images/images/player/MB-69/player1.png")

e = Enemy(200 , 40)
e.image = pygame.image.load("images/enemy/bacteria/bacteria1.png")

add(player)
add(e)

bullets = []

background_image = pygame.image.load("images/background/background.png")






# right_pressed = False
# left_pressed = False
# up_pressed = False
# down_pressed = False
# x_pressed = False

loop = True




while loop:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            loop = False
        else:
            input_manager.update(event)


    if input_manager.x_pressed:
    # 1. Creat a new bullet
        bullet = PlayerBullet(player.x , player.y)
        bullet.image = pygame.image.load("images/bullet/player/mb69bullet1.png")
    # 2. Add the newly created bullet into 'bullets' list
    #     bullets.append(bullet)
        add(bullet)

    # Bullets fly
    # Bullets draw

    update()

    for bullet in bullets:
        bullet.y -= 10
    for bullet in bullets:
        canvas.blit(bullet.image, (bullet.x - 48 / 2, bullet.y - 80 / 2))

    canvas.blit(background_image, (0, 0))

    render(canvas)




    pygame.display.flip()


    clock.tick(60)




