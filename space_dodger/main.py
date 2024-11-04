import pygame
import random
import time

pygame.font.init()

WIDTH, HEIGHT = 1300, 600
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Space Dodger")

BACKGROUND = pygame.transform.scale(
    pygame.image.load("kenya_nightsky.jpg"), (WIDTH, HEIGHT)
)  # pygame.image.load("kenya_nightsky.jpg")

PLAYER_HEIGHT = 60
PLAYER_WIDTH = 40
PLAYER_VELOCITY = 5

clock = pygame.time.Clock()

start_time = time.time()
elapsed_time = 0
end_time = time.time() - start_time

FONT = pygame.font.SysFont("roboto", 30)


def draw(player, elapsed_time):
    WINDOW.blit(BACKGROUND, (0, 0))  # Draw background

    elapsed_time_text = FONT.render(
        f"Elapsed Time: {round(elapsed_time)}s", True, "white"
    )
    WINDOW.blit(elapsed_time_text, (10, 10))

    pygame.draw.rect(WINDOW, "red", player)
    pygame.display.update()  # Update the display


def main():
    run = True

    player = pygame.Rect(650, HEIGHT - PLAYER_HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT)
    player.center = (
        WIDTH // 2,
        HEIGHT - 50,
    )  # Centers the player and lifts it slightly from the bottom

    while run:  # Game loop
        clock.tick(60)  # Sets the FPS to 60
        elapsed_time = time.time() - start_time
        # Event handling MUST be inside the loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.x - PLAYER_VELOCITY >= 0:
            player.x -= PLAYER_VELOCITY
        if keys[pygame.K_RIGHT] and player.x + PLAYER_VELOCITY <= WIDTH - PLAYER_WIDTH:
            player.x += PLAYER_VELOCITY
        draw(player, elapsed_time)
    pygame.quit()


if __name__ == "__main__":
    main()
