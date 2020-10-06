from pico2d import *
from gobj import *
import gfw

# 01 - 111  02,03 - 135

def enter():
    global cookie,jellys
    cookie = Cookie(111)
    cookie.image = load_image('../res/cookie/cookie01_run.png')
    #jellys = [ ]

def update():
    cookie.update()
#    for b in jellys: b.update()

def draw():
    cookie.draw()
    #    for b in jellys: b.draw()

def handle_event(e):
    global running
    if e.type == SDL_QUIT:
        gfw.quit()
    elif (e.type, e.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
        gfw.pop()

def exit():
    pass

if __name__ == '__main__':
    gfw.run_main()