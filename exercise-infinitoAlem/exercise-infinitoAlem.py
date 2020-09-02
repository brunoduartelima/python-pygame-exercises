import pygame
pygame.init()
window = pygame.display.set_mode([800, 580])

spaceship = pygame.image.load('spaceship.png')

quadX = 350
quadY = 400
speedX = 0
speedY = 0

clock = pygame.time.Clock()

while True:
  for event in pygame.event.get():
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_LEFT:        
        speedX = -1
      if event.key == pygame.K_RIGHT:
        speedX = 1
    if event.type == pygame.KEYUP:
      if (event.key == pygame.K_LEFT
        or event.key == pygame.K_RIGHT):
          speedX = 0

  window.fill((255, 255, 255))

  window.blit(spaceship, [quadX, quadY])

  quadX += speedX

  if quadX < -20 or quadX > 700:
    speedX = -speedX
  
  pygame.display.update()
  clock.tick(60)