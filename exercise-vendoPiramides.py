import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

vertices = (
  (1, 0, 1),
  (1, 0, -1),
  (-1, 0, -1),
  (-1, 0, 1),
  (0, 1, 0),
)

arestas = (
  (0, 1),
  (0, 3),
  (0, 4),
  (4, 1),
  (4, 2),
  (4, 3),
  (1, 2),
  (2, 3),
)

faces = (
  (0, 1, 4),
  (0, 3, 4),
  (1, 2, 4),
  (2, 3, 4),
  (0, 1, 2, 3)
)

def Piramide():
  glBegin(GL_POLYGON)
  for face in faces:
    for vertice in face:
      glColor3fv((0, 0, 1))
      glVertex3fv(vertices[vertice])
  glEnd()
  
  glBegin(GL_LINES)
  for aresta in arestas:
    for vertice in aresta:
      glColor3fv((0, 0, 0))
      glVertex3fv(vertices[vertice])
  glEnd()

pygame.init()
pygame.display.set_mode([800, 600], DOUBLEBUF|OPENGL)

gluPerspective(45, (800/600), 0, 50)
glTranslatef(0, 0, -5)

x_move = y_move = z_move = 0
x_camera = y_camera = z_camera = 0
camera_move = 0

while True:
  for event in pygame.event.get():
    if event.type == pygame.KEYDOWN:
      
      if event.key == pygame.K_LEFT:
        x_move = 0.1
      if event.key == pygame.K_RIGHT:
        x_move = -0.1
      
      if event.key == pygame.K_UP:
        camera_move = 1
        x_camera = 1
      if event.key == pygame.K_DOWN:
        camera_move = -1
        x_camera = 1
      
      if event.key == pygame.K_a:
        camera_move = 1
        y_camera = 1
      if event.key == pygame.K_d:
        camera_move = -1
        y_camera = 1

      if event.key == pygame.K_w:
        z_move = 0.1
      if event.key == pygame.K_s:
        z_move = -0.1
    
    if event.type == pygame.KEYUP:
      
      if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
        x_move = 0
      
      if event.key == pygame.K_w or event.key == pygame.K_s:
        z_move = 0
      
      if event.key == pygame.K_a or event.key == pygame.K_d or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
        camera_move = y_camera = x_camera = 0

  glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

  glTranslatef(x_move, y_move, z_move)
  glRotatef(camera_move, x_camera, y_camera, z_camera)
  
  Piramide()
  
  pygame.display.flip()
  pygame.time.wait(10)