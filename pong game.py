import pygame
import random

SCREEN_WIDTH = 960
SCREEN_HEIGHT = 720

COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)

# Initialize Pygame
pygame.init()

# Create the game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pong")

# Create the paddles
paddle_1_rect = pygame.Rect(30, 0, 7, 100)
paddle_2_rect = pygame.Rect(SCREEN_WIDTH - 50, 0, 7, 100)

# Initialize paddle movement variables
paddle_1_move = 0
paddle_2_move = 0

# Create the ball
ball_rect = pygame.Rect(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, 25, 25)

# Determine the initial ball velocity
ball_accel_x = random.randint(2, 4) * 0.1
ball_accel_y = random.randint(2, 4) * 0.1

# Randomize the direction of the ball
if random.randint(1, 2) == 1:
  ball_accel_x *= -1
if random.randint(1, 2) == 1:
  ball_accel_y *= -1

# Game loop
running = True
clock = pygame.time.Clock()

while running:
  # Handle events
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    elif event.type == pygame.KEYDOWN:
      if event.key == pygame.K_w:
        paddle_1_move = -0.5
      elif event.key == pygame.K_s:
        paddle_1_move = 0.5
      elif event.key == pygame.K_UP:
        paddle_2_move = -0.5
      elif event.key == pygame.K_DOWN:
        paddle_2_move = 0.5
    elif event.type == pygame.KEYUP:
      if event.key == pygame.K_w or event.key == pygame.K_s:
        paddle_1_move = 0.0
      elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
        paddle_2_move = 0.0

  # Update paddle positions
  paddle_1_rect.y += paddle_1_move * clock.get_time()
  paddle_2_rect.y += paddle_2_move * clock.get_time()

  # Ensure paddles stay within the screen bounds
  paddle_1_rect.y = max(0, min(paddle_1_rect.y, SCREEN_HEIGHT - paddle_1_rect.height))
  paddle_2_rect.y = max(0, min(paddle_2_rect.y, SCREEN_HEIGHT - paddle_2_rect.height))

  # Update ball position
  ball_rect.x += ball_accel_x * clock.get_time()
  ball_rect.y += ball_accel_y * clock.get_time()

  # Check for ball collision with paddles
  if paddle_1_rect.colliderect(ball_rect) and ball_accel_x < 0:
    ball_accel_x *= -1
  elif paddle_2_rect.colliderect(ball_rect) and ball_accel_x > 0:
    ball_accel_x *= -1

  # Check for ball collision with top and bottom walls
  if ball_rect.top <= 0 or ball_rect.bottom >= SCREEN_HEIGHT:
    ball_accel_y *= -1

  # Check for ball going out of bounds
  if ball_rect.left <= 0 or ball_rect.right >= SCREEN_WIDTH:
    # Reset ball position and velocity
    ball_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    ball_accel_x = random.randint(2, 4) * 0.1
    ball_accel_y = random.randint(2, 4) * 0.1
    if random.randint(1, 2) == 1:
      ball_accel_x *= -1
    if random.randint(1, 2) == 1:
      ball_accel_y *= -1

  # Clear the screen
  screen.fill(COLOR_BLACK)

  # Draw paddles and ball
  pygame.draw.rect(screen, COLOR_WHITE, paddle_1_rect)
  pygame.draw.rect(screen, COLOR_WHITE, paddle_2_rect)
  pygame.draw.rect(screen, COLOR_WHITE, ball_rect)

  # Update the display
  pygame.display.flip()

  # Limit the frame rate
  clock.tick(60)

# Quit the game
pygame.quit()

