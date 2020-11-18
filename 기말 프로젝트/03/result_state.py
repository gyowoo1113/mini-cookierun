import gfw
from pico2d import *
import gobj
from background import Background
import ready_state
from score import Score

def add(score):
    global scores
    cw = get_canvas_width()
    ch = get_canvas_height()
    scores = Score(cw/2.5,ch/2,(255,255,250),120)
    scores.score = score
    gfw.world.add(gfw.layer.score,scores)

def build_world():
    gfw.world.init(['bg','score'])
    bg = Background('map_bg/result_bg.png','../res/sound/result.wav','wav')
    gfw.world.add(gfw.layer.bg, bg)

def enter():
    build_world()

def update():
    gfw.world.update()

def draw():
    gfw.world.draw()

def handle_event(e):
    if e.type == SDL_QUIT:
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