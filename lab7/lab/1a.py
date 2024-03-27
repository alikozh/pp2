import pygame
from datetime import datetime

pygame.init()
screen = pygame.display.set_mode((829, 836))
done = False

bg_image = pygame.image.load('MicrosoftTeams-image (2).png')
sec_img = pygame.image.load('MicrosoftTeams-image (1).png')
min_img = pygame.image.load('MicrosoftTeams-image.png')

rect = bg_image.get_rect(center=(415, 418))

while not done:
    screen.blit(bg_image, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    time = datetime.now().time()


    sec_angle = -(time.second * 6)
    newsec_img = pygame.transform.rotate(sec_img, sec_angle)
    sec_rect = newsec_img.get_rect(center=rect.center)
    screen.blit(newsec_img, sec_rect.topleft)


    min_angle = -(time.minute * 6)
    nmin_img = pygame.transform.rotate(min_img, min_angle)
    min_rect = nmin_img.get_rect(center=rect.center)
    screen.blit(nmin_img, min_rect.topleft)

    pygame.display.flip()