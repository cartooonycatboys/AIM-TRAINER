import pgzrun
import random

TITLE="good shot"

WIDTH=550
HEIGHT=550
score=0
message=""
alien=Actor("alien")

def place_alien():
    alien.x=random.randint(50,WIDTH-50)
    alien.y=random.randint(50,HEIGHT-50)

def draw():
    screen.clear()
    screen.fill("cyan")
    alien.draw()
    screen.draw.text(message,center=(200,200),fontsize=30)
    screen.draw.text(f"Score:{score}",(20,0),fontsize=25)

def update():
    pass


def on_mouse_down(pos):
    global message,score
    if alien.collidepoint(pos):
        place_alien()
        message="good shot"
        score+=1
    else:
        message="you missed"
        score-=1

place_alien()
pgzrun.go()