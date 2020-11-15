import gfw
from pico2d import *
import gobj
import ready_state

canvas_width= 1120
canvas_height = 630

def build_world():
    global image
    image = load_image('../res/map_bg/title.png')

def enter():
    build_world()

def update():
    pass

def draw():
    image.draw_to_origin(0,0,get_canvas_width(),get_canvas_height())

def handle_event(e):
    if e.type == SDL_QUIT:
        gfw.quit()
    elif (e.type, e.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
        gfw.quit()
    elif (e.type, e.key) == (SDL_KEYDOWN, SDLK_SPACE):
        gfw.push(ready_state)

def exit():
    global image
    del image

def pause():
    pass

def resume():
    pass

if __name__ == '__main__':
    gfw.run_main()
