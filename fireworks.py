from pygame.sprite import Sprite
from colors import Colors
from random import choice
import pygame as pg

colors = Colors()
selection = 0
selection_secondary = 0
fireworks_colors = [colors.red, colors.magenta, colors.blue, colors.green, colors.yellow, colors.black, colors.white]
fireworks_colors_secondary = [None, colors.red, colors.magenta, colors.blue, colors.green, colors.yellow, colors.black, colors.white]
WIDTH = 1000
HEIGHT = 800
screen = pg.display.set_mode([WIDTH, HEIGHT])
pg.display.set_caption('Fireworks!')
fireworks = []
explosions = []
clock = pg.time.Clock()
flame_sizes = [2, 4, 6, 8, 10]


def render_choices():
    x_pos = 10
    for i in fireworks_colors:
        pg.draw.rect(screen, i, [x_pos, HEIGHT - 50, 20, 20])
        x_pos += 20
    x_pos = 15 + 20 * selection
    pg.draw.rect(screen, colors.black, [x_pos, HEIGHT - 60, 10, 10])
    x_pos = 10
    for i in fireworks_colors_secondary:
        if i is not None:
            pg.draw.rect(screen, i, [x_pos, HEIGHT - 20, 20, 20])
        x_pos += 20
    x_pos = 15 + 20 * selection_secondary
    pg.draw.rect(screen, colors.black, [x_pos, HEIGHT - 30, 10, 10])


class Explosion(Sprite):
    def __init__(self, x, y, maxtime, index, color, sec_color):
        super(Explosion, self).__init__()
        self.x = x
        self.y = y
        self.size = 10
        self.time = 0
        self.maxtime = maxtime
        self.index = index
        self.color = color
        self.sec_color = sec_color

    def draw(self):
        pg.draw.circle(screen, self.color, [self.x, self.y], self.size * 2, 15)
        if self.sec_color is not None:
            pg.draw.circle(screen, self.sec_color, [self.x, self.y], self.size, 10)

    def progress(self):
        self.time += 1
        self.size += 2

    def finish(self):
        explosions.remove(self)
        for i in explosions:
            i.index -= 1


class Firework(Sprite):
    def __init__(self, maxtime, index, color, sec_color):
        super(Firework, self).__init__()
        self.x = pg.mouse.get_pos()[0]
        self.y = pg.mouse.get_pos()[1]
        self.time = 0
        self.index = index
        self.maxtime = maxtime
        self.color = color
        self.sec_color = sec_color

    def draw(self):
        pg.draw.circle(screen, colors.orange, [self.x, self.y], choice(flame_sizes))
        pg.draw.rect(screen, colors.white, [self.x - 10, self.y, 20, -35])
        pg.draw.rect(screen, self.color, [self.x - 10, self.y - 20, 20, -5])
        if self.sec_color is not None:
            pg.draw.rect(screen, self.sec_color, [self.x - 10, self.y - 10, 20, -5])
        pg.draw.polygon(screen, colors.brown,
                        [[self.x - 15, self.y - 35], [self.x, self.y - 50], [self.x + 15, self.y - 35]])

    def explode(self):
        fireworks.remove(self)
        for i in fireworks:
            i.index -= 1
        explosions.append(Explosion(self.x, self.y - 50, 25, len(explosions), self.color, self.sec_color))

    def move(self):
        self.time += 1
        self.y -= (self.time // 10 + 2) * 2


while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            quit()
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_RIGHTBRACKET:
                if selection_secondary == len(fireworks_colors_secondary) - 1:
                    selection_secondary = 0
                else:
                    selection_secondary += 1
                render_choices()

            elif event.key == pg.K_LEFTBRACKET:
                if selection_secondary < 1:
                    selection_secondary = len(fireworks_colors_secondary) - 1
                else:
                    selection_secondary -= 1
                render_choices()
        elif event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1:
                fireworks.append(Firework(50, len(fireworks), fireworks_colors[selection],
                                          fireworks_colors_secondary[selection_secondary]))
            elif event.button == 4:
                if selection == len(fireworks_colors) - 1:
                    selection = 0
                else:
                    selection += 1
                render_choices()

            elif event.button == 5:
                if selection < 1:
                    selection = len(fireworks_colors) - 1
                else:
                    selection -= 1
                render_choices()

    screen.fill(colors.gray)
    for i in fireworks:
        if i.y - 50 <= 0 or i.time == i.maxtime:
            i.explode()

        i.move()
        i.draw()
    for i in explosions:
        if i.time > i.maxtime:
            i.finish()

        i.progress()
        i.draw()

    render_choices()

    pg.display.flip()
    clock.tick(50)
