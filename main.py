import pygame, sys, random




# crosshair class
class Crosshair(pygame.sprite.Sprite):
    def __init__(self, img_path):
        super().__init__()
        self.image = pygame.image.load(img_path)
        self.rect = self.image.get_rect() # create rect to image
        self.gunshot = pygame.mixer.Sound("./assets/gunshot_6.wav") # load wav files for gunshot

    def shoot(self):
        self.gunshot.play() # function that play sounds
        pygame.sprite.spritecollide(crosshair, target_group, True)
    def update(self):
        self.rect.center = pygame.mouse.get_pos()


# target class
class Target(pygame.sprite.Sprite):
    def __init__(self, img_path, pos_x, pos_y):
        super().__init__()
        self.image = pygame.image.load(img_path)
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x, pos_y]


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

# TARGET
target_group = pygame.sprite.Group()
for target in range(20):
    new_target = Target("./assets/target_red1.png", random.randrange(0, screen_width), random.randrange(0, screen_height))
    target_group.add(new_target)


# main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            crosshair.shoot() # gun shot sound when mouse click

    pygame.display.flip()
    screen.blit(background, (0, 0)) # background
    target_group.draw(screen)
    crosshair_group.draw(screen) # crosshair
    crosshair_group.update()
    clock.tick(60)