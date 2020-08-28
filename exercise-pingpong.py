import pygame
pygame.init()
window = pygame.display.set_mode([800, 580])

quadX = 200
quadY = 200
speedX = 1
speedY = 1

clock = pygame.time.Clock()

while True:

  window.fill((255, 255, 255))

  pygame.draw.circle(window, 
  (255, 0, 0),
  [quadX, quadY],
  72
  )

  quadX += speedX
  quadY += speedY

  if quadX < 70 or quadX > 730:
    speedX = -speedX
  
  if quadY < 70 or quadY > 510:
    speedY = -speedY
  
  pygame.display.update()
  clock.tick(60)