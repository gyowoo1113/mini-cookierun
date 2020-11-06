import gfw
import os.path
from pico2d import *
import gobj
from player import Player
from background import HorzScrollBackground
from platform import Platform
from jelly import Jelly
import random
import stage_gen

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

    stage_gen.load(gobj.res('stage_01.txt'))

paused = False
def update():
    if paused:
        return
    gfw.world.update()

    dx = -250 * gfw.delta_time

    for layer in range(gfw.layer.platform, gfw.layer.item + 1):
        for obj in gfw.world.objects_at(layer):
            obj.move(dx)

    check_items()

    stage_gen.update(dx)
    for item in gfw.world.objects_at(gfw.layer.item):
        item.check_player()

def check_items():
    for item in gfw.world.objects_at(gfw.layer.item):
        if gobj.collides_box(player, item):
            gfw.world.remove(item)
            #player.check(item)
            break

def draw():
    gfw.world.draw()
    gobj.draw_collision_box()
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

    elif e.key == SDLK_p:
        global paused
        paused = not paused

    if player.handle_event(e):
        return

def exit():
    pass



if __name__ == '__main__':
    gfw.run_main()