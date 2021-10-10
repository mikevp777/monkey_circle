import random

import pygame as pygame


class MyCircle:
    def __init__(self, screen, color, radius):
        self.screen = screen
        self.color = color
        self.radius = radius

    def draw_circle_pygame(self, x, y):
        pygame.draw.circle(self.screen, self.color, [x, y], self.radius, 1)

    def draw_point(self, x, y):
        self.screen.set_at((x, y), self.color)

    def draw_circle_monkey(self, a, b):
        r = self.radius
        for x in range(a-r, a+r+1):
            self._draw_circle_points_at_x(x, a, b, r)

    def _draw_circle_points_at_x(self, x, a, b, r):
        y1, y2 = self._find_y(x, a, b, r)
        self.draw_point(x, y1)
        self.draw_point(x, y2)

    def _find_y(self, x, a, b, r):
        return 350, 150  # Почему бы и нет


def draw_all():
    screen_height = 600
    screen_width = 800
    pygame.init()
    screen = pygame.display.set_mode((screen_width, screen_height))
    screen.fill((10, 10, 30))
    running = True

    # pygame.display.flip()
    circle_color = (255, 0, 0)
    circle_radius = 100
    my_circle = MyCircle(screen, circle_color, circle_radius)

    clock = pygame.time.Clock()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # my_circle.draw_circle_pygame(*event.pos)
                # my_circle.draw_point(*event.pos)
                my_circle.draw_circle_monkey(*event.pos)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    running = False

        pygame.display.flip()  # Call flip() each frame.
        clock.tick(60)  # Limit the game to 60 fps.


if __name__ == '__main__':
    draw_all()
