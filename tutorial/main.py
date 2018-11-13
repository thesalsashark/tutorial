import random
import pygame

pygame.init()

# Define Colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

# Define window
display_width = 800
display_height = 600
screen = pygame.display.set_mode((display_width, display_height))
screen.fill(white)
clock = pygame.time.Clock()

cats_list = pygame.sprite.Group()
cheeses_list = pygame.sprite.Group()
all_sprites_list = pygame.sprite.Group()


class Mouse(pygame.sprite.Sprite):
    def __init__(self, xcor=None, ycor=None):
        super().__init__()
        if xcor is None:
            xcor = random.randrange(0, display_width)
        if ycor is None:
            ycor = random.randrange(0, display_height)
        self.xcor = xcor
        self.ycor = ycor
        self.image = pygame.image.load("mouse.gif")
        self.rect = self.image.get_rect().size
        screen.blit(self.image, (self.xcor, self.ycor))


class Cheese(pygame.sprite.Sprite):
    def __init__(self, xcor=None, ycor=None):
        super().__init__()
        if xcor is None:
            xcor = random.randrange(0, display_width)
        if ycor is None:
            ycor = random.randrange(0, display_height)
        self.xcor = xcor
        self.ycor = ycor
        self.image = pygame.image.load("cheese.gif")
        self.rect = self.image.get_rect().size
        screen.blit(self.image, (self.xcor, self.ycor))


class Cat(pygame.sprite.Sprite):
    def __init__(self, xcor=None, ycor=None):
        super().__init__()
        if xcor is None:
            xcor = random.randrange(0, display_width)
        if ycor is None:
            ycor = random.randrange(0, display_height)
        self.xcor = xcor
        self.ycor = ycor
        self.image = pygame.image.load("cat.gif")
        self.rect = self.image.get_rect().size
        screen.blit(self.image, (self.xcor, self.ycor))


def create_mouse():
    mouse = Mouse()
    # screen.blit(mouse.image, (mouse.xcor, mouse.ycor))


def create_cheese():
    no_of_cheese = random.randrange(10, 20)
    for i in range(no_of_cheese):
        cheese = Cheese()
        cheeses_list.add(cheese)
        # screen.blit(cheese.image, (cheese.xcor, cheese.ycor))


def create_cat():
    no_of_cats = random.randrange(1, 2)
    for i in range(no_of_cats):
        cat = Cat()
        cats_list.add(cat)
        # screen.blit(cat.image, (cat.xcor, cat.ycor))

def crash():
    print("You lose")

# create_mouse()
# create_cat()
# create_cheese()

def game_loop():
    # Mouse.rect = (random.randrange(0, display_width), random.randrange(0, display_height))
    # xcor = random.randrange(0, display_width)
    # ycor = random.randrange(0, display_height)

    game_exit = False

    while not game_exit:

        screen.fill(white)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        mouse = Mouse()
        no_of_cats = random.randrange(1, 2)
        for i in range(no_of_cats):
            cat = Cat()
        no_of_cheese = random.randrange(10, 20)
        for i in range(no_of_cheese):
            cheese = Cheese()

        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_RIGHT]:
            mouse.xcor += 5
        if pressed[pygame.K_LEFT]:
            mouse.xcor -= 5
        if pressed[pygame.K_UP]:
            mouse.ycor -= 5
        if pressed[pygame.K_DOWN]:
            mouse.ycor += 5

        if mouse.xcor > (display_width - mouse.get_width()) or mouse.xcor < 0:
            crash()

        # if enemy_y > display_height:
        #     enemy_y = 0 - enemy_height
        #     enemy_x = random.randrange(0, display_width)
        #
        # if cheese_y > display_height:
        #     cheese_y = 0 - enemy_height
        #     cheese_x = random.randrange(0, display_width)
        #
        # if y + player_height > enemy_y and y < enemy_y + enemy_height:
        #     if x + player_width > enemy_x and x < enemy_x + enemy_width:
        #         crash()
        #
        # if y + player_height > cheese_y and y < cheese_y + cheese_height:
        #     if x + player_width > cheese_x and x < cheese_x + cheese_width:
        #         win()
        #
        # create_mouse()
        # create_cat()
        # create_cheese()

        # cheeses_list.draw(screen)
        # cats_list.draw(screen)
        # all_sprites_list.draw(screen)
        # pygame.display.flip()

        pygame.display.update()
        clock.tick(60)

game_loop()

pygame.quit()
quit()