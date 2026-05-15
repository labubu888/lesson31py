import pygame


pygame.init()
SCREEN_WIDTH, SCREEN_HEIGHT = 500,500


display_surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('adding image and background image')


background_image = pygame.transform.scale(
    pygame.image.load('b').comvert(),(SCREEN_HEIGHT,SCREEN_WIDTH))

penguin_image = pygame.transform.scale(
    pygame.image.load('i').convert_alpha(),(200.200))
penguin_rect = penguin_image.get_rect(center=(SCREEN WIDTH // 2, SCREEN_HEIGHT // 2 - 30)) 




