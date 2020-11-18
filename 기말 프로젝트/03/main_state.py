import gfw
import os.path
from pico2d import *
import gobj
from player import Player
from background import HorzScrollBackground
from platform import Platform
from jelly import Jelly
from boss import Boss
from life_gauge import Life
from score import Score
import random
import stage_gen
import result_state

# ''
canvas_width= 1120
canvas_height = 630

def build_world():
    gfw.world.init(['bg','platform','enemy','boss','item','player','ui','life','score'])
    Player.load_all_images()
    Jelly.load_all_images()

    center = get_canvas_width() // 2, get_canvas_height() // 2

    for n, speed in [(1,10), (2,100), (3,150)]:
        bg = HorzScrollBackground('map_bg/bg_%d.png' % n,'../res/sound/main.mp3')
        bg.speed = speed
        gfw.world.add(gfw.layer.bg, bg)

    global player
    player = Player()
    gfw.world.add(gfw.layer.player, player)

    global font
    font = load_font(gobj.RES_DIR + 'font/CookieRun Regular.ttf', 30)

    global life
    life = Life()
    gfw.world.add(gfw.layer.life, life)

    global score
    score = Score(canvas_width/2-30, canvas_height - 65,(0,0,0),30)
    gfw.world.add(gfw.layer.score, score)

    stage_gen.load(gobj.res('stage_boss.txt'))

    global obs_sound,crash_sound
    obs_sound = load_wav(gobj.RES_DIR + 'sound/obs.wav')
    obs_sound.set_volume(50)
    crash_sound = load_wav(gobj.RES_DIR + 'sound/crash.wav')
    crash_sound.set_volume(30)

paused = False

def enter():
    build_world()

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
    check_obsBoss()

    stage_gen.update(dx)

    call_obj()
    if player.end:
        End()

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
            if player.mag != 1.0:
                    enemy.crash = True
                    score.display += 100
                    score.score +=100
                    crash_sound.play()
            else:
                enemy.hit = True
                life.life -= enemy.power
                obs_sound.play()

def check_obsBoss():
    for boss in gfw.world.objects_at(gfw.layer.boss):
        if boss.hit: continue
        if gobj.collides_box(player, boss):
            if boss.action in ['run'] :
                boss.hit = True
                life.life -= boss.power
                obs_sound.play()

def call_obj():
    for item in gfw.world.objects_at(gfw.layer.item):
        item.check_player()

    global boss
    if gfw.world.count_at(gfw.layer.boss) > 0:
        boss = gfw.world.object(gfw.layer.boss, 0)
        boss.check_ui()

    if gfw.world.count_at(gfw.layer.player) > 0:
        player = gfw.world.object(gfw.layer.player,0)
        player.check_ui()

def draw():
    gfw.world.draw()
    #gobj.draw_collision_box()

def handle_event(e):
    if e.type == SDL_QUIT:
        gfw.quit()
    elif (e.type, e.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
        gfw.pop()
    elif (e.type, e.key) == (SDL_KEYDOWN, SDLK_RETURN):
        End()
    elif e.key == SDLK_p:
        global paused
        paused = not paused

    if player.handle_event(e):
        return

def End():
    gfw.push(result_state)
    result_state.add(score.score)

def exit():
    pass
def pause():
    pass
def resume():
    pass
#    build_world()


if __name__ == '__main__':
    gfw.run_main()