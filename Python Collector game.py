import pygame

pygame.init()
 

white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
black = (0, 0, 0,)

X = 1000
Y = 500

display_surface = pygame.display.set_mode((X, Y))

pygame.display.set_caption('COLLECTOR GAME ALPHA 1.1')
 

font = pygame.font.Font('freesansbold.ttf', 32 )

text = font.render('COLLECTOR GAME ALPHA 1.1', True, black, white)
 

textRect = text.get_rect()

textRect.center = (X // 2, Y // 6)
 


while True:
 
    display_surface.fill(white)

    display_surface.blit(text, textRect)
 
    for event in pygame.event.get():
 

        if event.type == pygame.QUIT:
 
    
            pygame.quit()
 
          
            quit()
 
  
        pygame.display.update()
