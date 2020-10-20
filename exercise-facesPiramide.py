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
  glBegin(GL_QUADS)
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
glRotatef(45, 1, 1, 0)

while True:
  glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
  
  Piramide()
  
  pygame.display.flip()
  pygame.time.wait(10)