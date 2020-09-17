import pygame
import random
import sys

pygame.init()
window = pygame.display.set_mode([800, 580])

spaceship = pygame.image.load('spaceship.png')

quadX = random.randrange(0, 700)
quadY = 0
imgX = 350
imgY = 400

r = random.randrange(0, 255)
g = random.randrange(0, 255)
b = random.randrange(0, 255)

score = 0

speedX = 0

clock = pygame.time.Clock()

while True:
  for event in pygame.event.get():
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_LEFT:        
        speedX = -10
      if event.key == pygame.K_RIGHT:
        speedX = 10
    if event.type == pygame.KEYUP:
      if (event.key == pygame.K_LEFT
        or event.key == pygame.K_RIGHT):
          speedX = 0

  window.fill((255, 255, 255))

  pygame.draw.rect(
    window, (r, g, b), [quadX, quadY, 100, 150]
  )

  window.blit(spaceship, [imgX, imgY])

  imgX += speedX
  quadY += 2

  if imgY < quadY + 150 and imgY + 128 > quadY:
    if imgX < quadX + 100 and imgX + 128 > quadX:
      score += 1
      quadY = 0
      quadX = random.randrange(0, 700)
      r = random.randrange(0, 255)
      g = random.randrange(0, 255)
      b = random.randrange(0, 255)


  if score > 10 and score < 20:
    quadY += 3 
  elif score >= 20 and score < 40:
    quadY += 6 
  elif score >= 40:
    quadY += 10
  
  if quadY > 580:
    quadY = 0
    quadX = random.randrange(0, 700)
    score -= 1

  if score < 0:
    font = pygame.font.Font('freesansbold.ttf', 100)
    text = font.render('GAME OVER', True, (0, 0, 0))
    window.blit(text, [100, 100])
    pygame.display.update()
    pygame.time.wait(2000)
    sys.exit()

  fontScore = pygame.font.Font('freesansbold.ttf', 32)
  textScore = fontScore.render(
    'score: ' + str(score), True, (0, 0, 0)
  )
  window.blit(textScore, [20, 20])

  if imgX < -20 or imgX > 700:
    speedX = -speedX

  
  pygame.display.update()
  clock.tick(30)