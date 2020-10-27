import gfw
import os.path
from pico2d import *
from gobj import *
from player import Player
from background import HorzScrollBackground
from platform import Platform

canvas_width= 1120
canvas_height = 630

def enter():
    gfw.world.init(['bg','enemy','platform','item','player'])
    Player.load_all_images()

    center = get_canvas_width() // 2, get_canvas_height() // 2

    for n, speed in [(1,10), (2,100), (3,150)]:
        bg = HorzScrollBackground('map_bg/bg_%d.png' % n)
        bg.speed = speed
        gfw.world.add(gfw.layer.bg, bg)

    global player
    player = Player()
#    player.bg = bg
    gfw.world.add(gfw.layer.player, player)

#
    x = 0
    cw = 2 * get_canvas_width()
    while x < cw:
        t = Platform.T_6x7
        pf = Platform(t, x, 0)
        gfw.world.add(gfw.layer.platform, pf)
        x += pf.width


def update():
    gfw.world.update()


#    dx = -200 * gfw.delta_time

#    for layer in range(gfw.layer.enemy, gfw.layer.item + 1):
#        for obj in gfw.world.objects_at(layer):
#            obj.move(dx)

def draw():
    gfw.world.draw()
#    draw_collision_box()

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