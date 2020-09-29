import pygame
import sys

pygame.init()
window = pygame.display.set_mode([800, 580])

quadX = 100
quadY = 175

movX = 0
movY = 0

clock = pygame.time.Clock()

while True:
  for event in pygame.event.get():
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_LEFT:
        movX = -1
      if event.key == pygame.K_RIGHT:
        movX = 1
      if event.key == pygame.K_UP:
        movY = -1
      if event.key == pygame.K_DOWN:
        movY = 1
    if event.type == pygame.KEYUP:
      if (event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT):
        movX = 0
      if(event.key == pygame.K_UP or event.key == pygame.K_DOWN):
        movY = 0
      
  
  window.fill((150, 200, 180))

  pygame.draw.rect(window, (0, 0, 0),
    [0, 150, 600, 100]
  )

  pygame.draw.rect(window, (0, 0, 0),
    [500, 250, 100, 330]
  )

  pygame.draw.rect(window, (255, 255, 255),
    [quadX, quadY, 50, 50]
  )

  quadX += movX
  quadY += movY

  font = pygame.font.Font('freesansbold.ttf', 150)

  if quadY < 150 or quadX + 50 > 600 or (quadY + 50 > 250 and quadX < 500) or (quadY > 250 and quadX < 500):
    text = font.render('PERDEU', True, (255, 0, 0))
    window.blit(text, [100, 50])
    pygame.display.update()
    pygame.time.wait(2000)
    sys.exit()

  if quadY + 50 > 580:
    text = font.render('GANHOU', True, (50, 200, 50))
    window.blit(text, [50, 50])
    pygame.display.update()
    pygame.time.wait(2000)
    sys.exit()

  pygame.display.update()
  clock.tick(60)