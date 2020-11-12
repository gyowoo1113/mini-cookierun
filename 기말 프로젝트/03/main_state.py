import gfw
import os.path
from pico2d import *
import gobj
from player import Player
from background import HorzScrollBackground
from platform import Platform
from jelly import Jelly
from boss import Boss
import random
import stage_gen

canvas_width= 1120
canvas_height = 630

def enter():
    gfw.world.init(['bg','platform','enemy','boss','item','player'])
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

    stage_gen.load(gobj.res('stage_boss.txt'))

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
    check_obstacles()

    stage_gen.update(dx)
    for item in gfw.world.objects_at(gfw.layer.item):
        item.check_player()

    global boss
    if gfw.world.count_at(gfw.layer.boss) > 0:
        boss = gfw.world.object(gfw.layer.boss, 0)

def check_items():
    for item in gfw.world.objects_at(gfw.layer.item):
        if gobj.collides_box(player, item):
            gfw.world.remove(item)
            player.check(item)
            if gfw.world.count_at(gfw.layer.boss) > 0:
                boss.check(item)
            break

def check_obstacles():
    for enemy in gfw.world.objects_at(gfw.layer.enemy):
        if enemy.hit: continue
        if enemy.crash: continue
        if gobj.collides_box(player, enemy):
            if player.SUPER:
                enemy.crash = True
                player.score +=100
            else:
                enemy.hit = True
                # 체력바 감소 추가

def check_obsBoss():
    pass                #충돌체크 -> hit true로 변경될때 self.cnt = self.fdix

def draw():
    gfw.world.draw()
    gobj.draw_collision_box()
    font.draw(canvas_width/2-30, canvas_height - 45, '%d' % player.score)

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