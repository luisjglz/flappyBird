"""Flappy, game inspired by Flappy Bird.

Exercises

1. Keep score. done
2. Vary the speed. done
3. Vary the size of the balls. done
4. Allow the bird to move forward and back.

"""

from random import *
from turtle import *

from freegames import vector

bird = vector(0, 0)
balls = []
puntos = 0

def tap(x, y):
    """Move bird up in response to screen tap."""
    up = vector(0, 30)
    bird.move(up)


def inside(point):
    if (type(point) is dict):
        return -200 < point["pos"].x < 200 and -200 < point["pos"].y < 200
    else:    
        """Return True if point on screen."""
        return -200 < point.x < 200 and -200 < point.y < 200


def draw(alive):
    """Draw screen objects."""
    clear()

    goto(bird.x, bird.y)

    if alive:
        dot(10, 'green')
    else:
        dot(10, 'red')

    for ball in balls:
        goto(ball["pos"].x, ball["pos"].y)
        dot(ball["tam"], 'black')

    """
    Mostrar el puntaje en la pantalla
    Primero muevo el puntero (turtle)
    hacia el lugar donde quiero mostrar
    el marcador y luego lo escribo en pantalla.
    """
    goto(160,170)
    write(puntos, move=False, align='left', font=('Arial', 18, 'normal')) 



    update()


def move():
    """Update object positions."""
    bird.y -= 5

    for ball in balls:
        ball["pos"].x -= ball["vel"]

    if randrange(20) == 0:
        y = randrange(-199, 199)
        ball = {"pos":vector(199, y),"vel":randrange(3,8),"tam":randrange(15,25)}
        balls.append(ball)

    while len(balls) > 0 and not inside(balls[0]):
        balls.pop(0)
        """
        Hice punto (salió el ball por la izq)
        Especificar "global" para que modifique
        la variable puntos definida al inicio.
        """
        global puntos
        puntos += 1


    if not inside(bird):
        draw(False)
        return

    for ball in balls:
        if abs(ball["pos"] - bird) < 15:
            draw(False)
            return

    draw(True)
    ontimer(move, 50)


setup(420, 420, 370, 0)
hideturtle()
up()
tracer(False)
onscreenclick(tap)
move()
done()
