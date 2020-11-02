import gfw
import os.path
from pico2d import *
import gobj
from player import Player
from background import HorzScrollBackground
from platform import Platform
from jelly import Jelly
import random

canvas_width= 1120
canvas_height = 630

def enter():
    gfw.world.init(['bg','enemy','platform','item','player'])
    Player.load_all_images()
    Jelly.load_all_images()

    center = get_canvas_width() // 2, get_canvas_height() // 2

    for n, speed in [(1,10), (2,100), (3,150)]:
        bg = HorzScrollBackground('map_bg/bg_%d.png' % n)
        bg.speed = speed
        gfw.world.add(gfw.layer.bg, bg)

    global player
    player = Player()
#    player.bg = bg
    gfw.world.add(gfw.layer.player, player)

    global font
    font = load_font(gobj.RES_DIR + 'font/CookieRun Regular.ttf', 40)




def update():
    gfw.world.update()

    move_platform()

def move_platform():

    x = 0
    dx = -200 * gfw.delta_time
    for layer in range(gfw.layer.enemy, gfw.layer.item + 1):
        for obj in gfw.world.objects_at(layer):
            obj.move(dx)
            if hasattr(obj, 'right'):
                r = obj.right
                if x < r: x = r

    check_items()

    cw = 2 * get_canvas_width()
    while x < cw:
        t = Platform.T_6x7
        pf = Platform(t, x, 0)
        gfw.world.add(gfw.layer.platform, pf)

        # 임시로 랜덤선택 해놓음
        type = random.choice(['jelly','jelly','jelly','jelly','magnet'])

        jelly = Jelly(type, x + pf.width // 2, random.randint(200, 500))
        gfw.world.add(gfw.layer.item, jelly)
        # print('adding platform:', gfw.world.count_at(gfw.layer.platform))
        x += pf.width

def check_items():
    for item in gfw.world.objects_at(gfw.layer.item):
        if gobj.collides_box(player, item):
            gfw.world.remove(item)
            player.check(item)
            break

def draw():
    gfw.world.draw()
    #gobj.draw_collision_box()
    font.draw(canvas_width/2, canvas_height - 45, '%d' % player.score)

def handle_event(e):
    # prev_dx = boy.dx
    if e.type == SDL_QUIT:
        gfw.quit()
        return
    elif e.type == SDL_KEYDOWN:
        if e.key == SDLK_ESCAPE:
            gfw.pop()
            return

    if player.handle_event(e):
        return

def exit():
    pass



if __name__ == '__main__':
    gfw.run_main()