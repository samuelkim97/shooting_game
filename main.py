import pygame, sys



# crosshair class
class Crosshair(pygame.sprite.Sprite):
    def __init__(self, img_path):
        super().__init__()
        self.image = pygame.image.load(img_path)
        self.rect = self.image.get_rect() # create rect to image

    def update(self):
        self.rect.center = pygame.mouse.get_pos()



# general setup
pygame.init()
clock = pygame.time.Clock()

# display
screen_width = 1920
screen_height = 1000
screen = pygame.display.set_mode((screen_width, screen_height))
background = pygame.image.load("./assets/bg_blue.png")
background = pygame.transform.scale(background, (screen_width, screen_height))
pygame.mouse.set_visible(False) # invisible mouse




# CROSSHAIR
crosshair = Crosshair("./assets/crosshair_outline_small.png") # create object
crosshair_group = pygame.sprite.Group() # group objects
crosshair_group.add(crosshair) # added to group 


# main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.flip()
    screen.blit(background, (0, 0))
    crosshair_group.draw(screen)
    crosshair_group.update()
    clock.tick(60)