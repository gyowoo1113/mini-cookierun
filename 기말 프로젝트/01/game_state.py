from pico2d import *
from gobj import *
import gfw

# 01 - 111  02,03 - 135
# layer1 - 1075x369, layer2 - 1075x372
# bottom = back과는 다른 객체로 구분

def enter():
    global cookie,jellys,back1,back2,bottom
    cookie = Cookie(135)
    cookie.image = load_image('../res/cookie/example/cookie03_run.png')
    cookie.image2 = load_image('../res/cookie/example/cookie03_jump.png')
    back1 = Back(1)
    back2 = Back(2)
    back1.image = load_image('../res/map_bg/back_layer01.png')
    back2.image = load_image('../res/map_bg/back_layer02.png')
    #bottom = Back(2,(4,100))
    #bottom.image = load_image('../res/map_bg/bottom.png')

def update():
    back1.update()
    back2.update()
    #bottom.update()
    cookie.update()

def draw():
    back1.draw()
    back2.draw()
    cookie.draw()
    #bottom.draw()

def handle_event(e):
    global running
    if e.type == SDL_QUIT:
        gfw.quit()
    elif (e.type, e.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
        gfw.pop()
    cookie.handle_event(e)

def exit():
    pass

if __name__ == '__main__':
    gfw.run_main()