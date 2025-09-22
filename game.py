import pygame, sys, random
pygame.init()

# Setup
W, H = 400, 300
win = pygame.display.set_mode((W, H))
pygame.display.set_caption("Mini Pong - JB.PY")

# Colors
WHITE, BLACK = (0, 128, 0), (0,0,0)

# Ball
ball = pygame.Rect(W//2, H//2, 10, 10)
vx, vy = 2, 2   # slower speed

# Paddle
paddle = pygame.Rect(W//2-30, H-20, 60, 10)

# Game vars
lives = 3
font = pygame.font.SysFont(None, 24)
clock = pygame.time.Clock()

while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT: pygame.quit(); sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle.left > 0: paddle.move_ip(-4, 0)
    if keys[pygame.K_RIGHT] and paddle.right < W: paddle.move_ip(4, 0)

    ball.move_ip(vx, vy)

    # Bounce walls
    if ball.left <= 0 or ball.right >= W: vx = -vx
    if ball.top <= 0: vy = -vy

    # Paddle hit
    if ball.colliderect(paddle): vy = -vy

    # Miss ball
    if ball.bottom >= H:
        lives -= 1
        ball.topleft = (W//2, H//2)
        if lives == 0: pygame.quit(); sys.exit()

    # Draw
    win.fill(BLACK)
    pygame.draw.ellipse(win, WHITE, ball)
    pygame.draw.rect(win, WHITE, paddle)
    txt = font.render(f"Lives: {lives}", True, WHITE)
    win.blit(txt, (10, 10))
    pygame.display.flip()
    clock.tick(60)
