import pygame

pygame.init()

screen_width = 500
screen_height = 500
fps = 60

# Colors #
bg = (44, 53, 120)
white = (193, 200, 217)
black = (41, 42, 46)
blue_dark = (29, 96, 143)
blue_mid = (95, 68, 227)
blue_light = (53, 172, 212)

# Screen and Icon #
screen = pygame.display.set_mode([screen_width, screen_height])
pygame.time.Clock.tick(fps)
pygame.display.set_caption("Alarms and Timers")
windowIcon = pygame.image.load("clock.png")
pygame.display.set_icon(windowIcon)


# Main Function #
def main():
    running = True
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()

        screen.fill(bg)

        pygame.display.flip()


if __name__ == "__main__":
    main()
    pygame.quit()