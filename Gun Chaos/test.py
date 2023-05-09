import pygame
import math
from sheet import *
from pygame_functions import *

screen_width = 1200
screen_height = 800

pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Gun Chaos")
background_image = pygame.image.load('Images/MB.jpg')
background_image = pygame.transform.scale(background_image, (screen_width, screen_height))
BLACK=(0,0,0)

the_sheet = Spritesheet('Images/Sugnoma.png')
the_rev_sheet=Spritesheet('Images/Sugnoma_reverse.png')
first_player = the_sheet.get_sprite(0, 0, 128, 125)
second_player = the_sheet.get_sprite(128, 0, 128, 125)

left1_animations=[the_rev_sheet.get_sprite(896,128,128,128),
                 the_rev_sheet.get_sprite(896,256,128,128),
                 the_rev_sheet.get_sprite(896,384,128,128),
                 the_rev_sheet.get_sprite(896,512,128,128)]

right1_animations=[the_sheet.get_sprite(0,128,128,110),
                  the_sheet.get_sprite(0,256,128,110),
                  the_sheet.get_sprite(0,384,128,110),
                  the_sheet.get_sprite(0,512,128,110)]

left2_animations=[the_rev_sheet.get_sprite(768,128,128,128),
                 the_rev_sheet.get_sprite(768,256,128,128),
                 the_rev_sheet.get_sprite(768,384,128,128),
                 the_rev_sheet.get_sprite(768,512,128,128)]

right2_animations=[the_sheet.get_sprite(128,128,128,110),
                  the_sheet.get_sprite(128,256,128,110),
                  the_sheet.get_sprite(128,384,128,110),
                  the_sheet.get_sprite(128,512,128,110)]

anim_loop=1
first_player_rect = first_player.get_rect(topleft=(0, screen_height - 500))
second_player_rect = second_player.get_rect(topleft=(500, screen_height - 500))

gravity = 0.2
first_player_vel_y = 0.0
second_player_vel_y = 0.0


while True:
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    keys = pygame.key.get_pressed()

    # Move first player with arrow keys
    if keys[pygame.K_LEFT] :
        proposed_first_player_rect = first_player_rect.move(-2, 0)
        first_player=left1_animations[math.floor(anim_loop)]
        anim_loop+=0.01
        if anim_loop>=3:
            anim_loop=1
        if not proposed_first_player_rect.colliderect(second_player_rect):
            first_player_rect = proposed_first_player_rect
       

    # check for collisions with platforms
        """for platf in platf_list:
            if proposed_first_player_rect.colliderect(platf.rect):
                first_player_vel_y = 0
                first_player_rect.bottom = platf.rect.top"""
                

    if keys[pygame.K_RIGHT]:
        proposed_first_player_rect = first_player_rect.move(2, 0)
        first_player=right1_animations[math.floor(anim_loop)]
        anim_loop+=0.01
        if anim_loop>=3:
            anim_loop=1
        if not proposed_first_player_rect.colliderect(second_player_rect):
            first_player_rect = proposed_first_player_rect

        # check for collisions with platforms
        """for platf in platf_list:
            if proposed_first_player_rect.colliderect(platf.rect):
                first_player_vel_y = 0
                first_player_rect.bottom = platf.rect.top"""
            

    # Jump with up arrow key
    if keys[pygame.K_UP] and first_player_rect.bottom == screen_height:
        first_player_vel_y = -10

    first_player_vel_y += gravity
    proposed_rect = first_player_rect.move(0, int(first_player_vel_y))
    if not proposed_rect.colliderect(second_player_rect):
        first_player_rect = proposed_rect
    else:
        first_player_vel_y = 0.0
            # check for collisions with platforms
                

    if keys[pygame.K_q] :
        proposed_second_player_rect = second_player_rect.move(-2, 0)
        second_player=left2_animations[math.floor(anim_loop)]
        anim_loop+=0.01
        if anim_loop>=4:
            anim_loop=1
        if not proposed_second_player_rect.colliderect(first_player_rect):
            second_player_rect = proposed_second_player_rect

        # check for collisions with platforms
        """for platf in platf_list:
            if proposed_second_player_rect.colliderect(platf.rect):
                second_player_vel_y = 0
                second_player_rect.bottom = platf.rect.top"""
                

    if keys[pygame.K_d]:
        proposed_second_player_rect = second_player_rect.move(2, 0)
        second_player=right2_animations[math.floor(anim_loop)]
        anim_loop+=0.01
        if anim_loop>=4:
            anim_loop=1
        if not proposed_second_player_rect.colliderect(first_player_rect):
            second_player_rect = proposed_second_player_rect
        """for platf in platf_list:
            platf.update_rect()
            if proposed_first_player_rect.colliderect(platf.rect):
                first_player_vel_y = 0
                first_player_rect.bottom = platf.rect.top
            if proposed_second_player_rect.colliderect(platf.rect):
                second_player_vel_y = 0
                second_player_rect.bottom = platf.rect.top"""
                

    # Jump with W key
    if keys[pygame.K_z] and second_player_rect.bottom == screen_height:
        second_player_vel_y = -10

    second_player_vel_y += gravity
    proposed_rect = second_player_rect.move(0, int(second_player_vel_y))
    if not proposed_rect.colliderect(first_player_rect):
        second_player_rect = proposed_rect
    else:
        second_player_vel_y = 0.0




    # Prevent players from moving off the screen
    if first_player_rect.left < 0:
        first_player_rect.left = 0
    if first_player_rect.right > screen_width:
        first_player_rect.right = screen_width
    if first_player_rect.top < 0:
        first_player_rect.top = 0
    if first_player_rect.bottom > screen_height:
        first_player_rect.bottom = screen_height

    if second_player_rect.left < 0:
        second_player_rect.left = 0
    if second_player_rect.right > screen_width:
        second_player_rect.right = screen_width
    if second_player_rect.top< 0:
        second_player_rect.top = 0
    if second_player_rect.bottom > screen_height:
        second_player_rect.bottom = screen_height
    
    
    screen.fill((0, 0, 0))
    screen.blit(background_image,(0,0))
    screen.blit(first_player,first_player_rect )
    screen.blit(second_player, second_player_rect)
    pygame.display.update()
            