import gfw
from pico2d import *
import gobj
from background import Background
import main_state

#임시
canvas_width= 1120
canvas_height = 630

def build_world():
    gfw.world.init(['bg',])
    bg = Background('map_bg/ready_bg.png','../res/sound/ready.mp3','mp3')
    gfw.world.add(gfw.layer.bg, bg)

    global frame_interval
    frame_interval = gfw.frame_interval
    gfw.frame_interval = 0

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
        gfw.pop()
    elif (e.type, e.key) == (SDL_KEYDOWN, SDLK_SPACE):
        gfw.push(main_state)

def exit():
    global frame_interval
    gfw.frame_interval = frame_interval

def pause():
    pass

def resume():
    build_world()

if __name__ == '__main__':
    gfw.run_main()
