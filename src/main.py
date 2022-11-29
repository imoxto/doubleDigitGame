import pygame as pgm
import pygame.locals as pgmlc
import OpenGL.GL as gl
import OpenGL.GLU as glu

from doubleDigit import drawNumber
from settings import DISPLAY_SIZE, A_RATIO
from cube import cube


def main():
    pgm.init()
    pgm.display.set_mode(DISPLAY_SIZE, pgmlc.DOUBLEBUF | pgmlc.OPENGL)

    glu.gluPerspective(45, A_RATIO, 0.1, 50.0)
    gl.glTranslatef(0.0, 0.0, -5)
    gl.glRotatef(0,0,0,0)
    n=50
    while True:
        for event in pgm.event.get():
            if event.type == pgm.QUIT:
                pgm.quit()
                quit()
            if event.type == pgm.KEYDOWN:
                if event.key == pgm.K_UP:
                    n=n+1
                elif event.key == pgm.K_DOWN:
                    n=n-1
                elif event.key == pgm.K_LEFT:
                    gl.glTranslatef(-0.5, 0.0, 0)
                elif event.key == pgm.K_RIGHT:
                    gl.glTranslatef(0.5, 0.0, 0)
                elif event.key == pgm.K_w:
                    gl.glRotate(15,0,0,1)
                elif event.key == pgm.K_s:
                    gl.glRotate(-15,0,0,1)
                elif event.key == pgm.K_a:
                    gl.glRotate(15,0,1,0)
                elif event.key == pgm.K_d:
                    gl.glRotate(-15,0,1,0)
                elif event.key == pgm.K_q:
                    gl.glRotate(15,1,0,0)
                elif event.key == pgm.K_e:
                    gl.glRotate(-15,1,0,0)
            if event.type == pgm.MOUSEBUTTONDOWN:
                if event.button == 4:
                    gl.glTranslatef(0.0, 0.0, -1)
                elif event.button == 5:
                    gl.glTranslatef(0.0, 0.0, 1)

        
        gl.glClear(gl.GL_COLOR_BUFFER_BIT|gl.GL_DEPTH_BUFFER_BIT)
        gl.glBegin(gl.GL_POINTS)
        drawNumber(n)
        gl.glEnd()
        # cube()
        pgm.display.flip()
        pgm.time.wait(20)

main()