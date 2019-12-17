import pygame
import random

# Initialize pygame

pygame.init()


# Create a screen

screen = pygame.display.set_mode((800, 600))

# Background
background = pygame.image.load("images/background.png")

# Title and icon
pygame.display.set_caption("Space invaders")
icon = pygame.image.load("images/startup.png")
pygame.display.set_icon(icon)

# Enemy
enemyImg = pygame.image.load("images/ufo.png")
enemyX = random.randint(0, 800)
enemyY = random.randint(50, 150)
enemyX_change = 5
enemyY_change = 6

def enemy(x, y):
	screen.blit(enemyImg, (x,y))

# Enemy
bulletImg = pygame.image.load("images/bullet.png")
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 10

# Ready state means you cna't see the bullet state on the screen
# And fire the bullet is currently moving
bullet_state = 'ready'

def fire_bullet(x, y):
	global bullet_state
	bullet_state = 'fire'
	screen.blit(bulletImg, (x + 16, y + 10))

# Player
playerImg = pygame.image.load("images/space-invaders.png")
playerX = 370
playerY = 480
playerX_change = 0

def player(x, y):
	screen.blit(playerImg, (x, y))

# Game loop
running = True
while running:
	screen.fill((0, 0, 0))
	screen.blit(background, (80, 60))
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

		# If keystroke is pressed check wehther it's left or right
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				playerX_change = -5
			if event.key == pygame.K_RIGHT:
				playerX_change = 5
			if event.key == pygame.K_SPACE:
				fire_bullet(playerX, bulletY)
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
				playerX_change = 0

	playerX += playerX_change
	if playerX <= 0:
		playerX = 0
	elif playerX >= 736:
		playerX = 736

	enemyX += enemyX_change
	if enemyX <= 0:
		enemyY += enemyY_change
		enemyX_change = 5
	elif enemyX >= 736:
		enemyY += enemyY_change
		enemyX_change = -5

	# Bullet movement
	if bullet_state == 'fire':
		fire_bullet(playerX, bulletY)
		bulletY -= bulletY_change
	player(playerX, playerY)
	enemy(enemyX, enemyY)
	pygame.display.update()