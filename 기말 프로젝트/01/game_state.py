from pico2d import *
from gobj import *
import gfw

# 01 - 111  02,03 - 135
# layer1 - 1075x369, layer2 - 1075x372

def enter():
    global cookie,jellys,back1,back2,bottom
    cookie = Cookie(111)
    cookie.image = load_image('../res/cookie/cookie01_run.png')
    back1 = Back(1075,400,1,200)
    back2 = Back(1075,400,2,200)
    bottom = Back(1075,138,1,4)
    back1.image = load_image('../res/map_bg/back_layer01.png')
    back2.image = load_image('../res/map_bg/back_layer02.png')
    bottom.image = load_image('../res/map_bg/bottom.png')

    #jellys = [ ]

def update():
    back1.update()
    back2.update()
    bottom.update()
    cookie.update()
#    for b in jellys: b.update()

def draw():
    back1.draw()
    back2.draw()
    bottom.draw()
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