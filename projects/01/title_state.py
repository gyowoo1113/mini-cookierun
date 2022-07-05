import gfw
from pico2d import *
import ready_state


def enter():
    global image
    image = load_image('../res/map_bg/title.png')

def update():
    pass

def draw():
    image.draw(400,200,800,400)

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
