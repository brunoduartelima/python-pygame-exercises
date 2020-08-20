import pygame

pygame.init()

window = pygame.display.set_mode([800, 580])

while True:
  window.fill((255, 255, 255))

  pygame.draw.rect(
    window,
    (0, 0, 0),
    [100, 300, 200, 200],
    3
  )

  pygame.draw.polygon(
    window,
    (0, 0, 0),
    ((300,300),(380,275),(380,475),(300,499)),
    3
  )

  pygame.draw.polygon(
    window,
    (255, 0, 0),
    ((100,298),(300,298),(380,274),(250,150))
  )

  pygame.draw.line(
    window,
    (0, 0, 0),
    [250,150],
    [300, 300],
    3
  )

  pygame.draw.polygon(
    window,
    (200, 200, 200),
    ((320,330),(370,315),(370,360),(320,375))
  )
  
  pygame.draw.rect(
    window,
    (156, 128, 90),
    [200, 370, 80, 128]
  )

  pygame.draw.rect(
    window,
    (200, 200, 200),
    [120, 340, 60, 60]
  )

  pygame.draw.circle(
    window,
    (255, 221, 0),
    [650, 150],
    70
  )



  pygame.display.update()