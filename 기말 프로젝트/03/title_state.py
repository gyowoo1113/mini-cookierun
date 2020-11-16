import gfw
from pico2d import *
import gobj
from background import Background
import ready_state

canvas_width= 1120
canvas_height = 630

def build_world():
    gfw.world.init(['bg',])
    bg = Background('../res/map_bg/title.png','../res/sound/title.wav','wav')
    gfw.world.add(gfw.layer.bg, bg)

def enter():
    build_world()

def update():
    pass

def draw():
    gfw.world.draw()

def handle_event(e):
    if e.type == SDL_QUIT:
        gfw.quit()
    elif (e.type, e.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
        gfw.quit()
    elif (e.type, e.key) == (SDL_KEYDOWN, SDLK_SPACE):
        gfw.push(ready_state)

def exit():
    pass

def pause():
    pass

def resume():
    build_world()

if __name__ == '__main__':
    gfw.run_main()
