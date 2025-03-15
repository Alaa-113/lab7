import pygame
import time

pygame.init()

width, height = 600, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Mickey Mouse Clock")

mickey_body = pygame.image.load("micky/mickey.png").convert_alpha()
right_hand = pygame.image.load("right_hand-removebg-preview.png").convert_alpha()
left_hand = pygame.image.load("left.png").convert_alpha()

mickey_center = (width // 2, height // 2)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    current_time = time.localtime()
    minutes = current_time.tm_min
    seconds = current_time.tm_sec

    minutes_angle = -(minutes * 6 + 60)  
    seconds_angle = -seconds * 6  

    rotated_right_hand = pygame.transform.rotate(right_hand, minutes_angle)
    rotated_left_hand = pygame.transform.rotate(left_hand, seconds_angle)

    rotated_right_rect = rotated_right_hand.get_rect(center=mickey_center)
    rotated_left_rect = rotated_left_hand.get_rect(center=mickey_center)

    screen.fill((255, 255, 255))
    screen.blit(mickey_body, mickey_body.get_rect(center=mickey_center))
    screen.blit(rotated_right_hand, rotated_right_rect)
    screen.blit(rotated_left_hand, rotated_left_rect)

    pygame.display.flip()
    pygame.time.delay(100)

pygame.quit()
