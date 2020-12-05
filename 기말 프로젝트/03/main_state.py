import gfw
import os.path
from pico2d import *
import gobj
from player import Player
from background import HorzScrollBackground,Pro
from platform import Platform
from jelly import Jelly
from boss import Boss
from life_gauge import Life
from score import Score
from button import Button
import random
import stage_gen
import result_state

# ''
canvas_width= 1120
canvas_height = 630

def add(n):
    global name
    name = n

def pause_set():
    global paused,open
    paused = not paused
    open = not open
    if open:
        init_menu()
    else:
        kontinue()

def build_world():
    gfw.world.init(['bg','platform','enemy','boss','item','player','life','score','ui','menu'])
    Player.load_all_images()
    Jelly.load_all_images()

    center = get_canvas_width() // 2, get_canvas_height() // 2

    for n, speed in [(1,10), (2,100), (3,150)]:
        bg = HorzScrollBackground('map_bg/bg_%d.png' % n,'../res/sound/main.mp3')
        bg.speed = speed
        gfw.world.add(gfw.layer.bg, bg)

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

    global player
    player = Player(name)
    gfw.world.add(gfw.layer.player, player)

    l,b,w,h = get_canvas_width()-100,get_canvas_height()-100,50,50
    btn = Button("pause_",l,b,w,h,font,"", lambda: pause_set())
    gfw.world.add(gfw.layer.ui, btn)

    global paused,open
    paused = False
    open = False

def init_menu():
    l,b,w,h = get_canvas_width()//3+80,get_canvas_height()//4,240,200
    menu_bg = Pro(gobj.RES_DIR +'map_bg/choose_bg.png',(l,b,w,h))
    gfw.world.add(gfw.layer.menu, menu_bg)

    l,b,w,h = get_canvas_width()//3+100,get_canvas_height()//4+10,200,50
    btn = Button("",l,b,w,h,font,"Return", lambda: gfw.pop())
    gfw.world.add(gfw.layer.menu, btn)

    l,b,w,h = get_canvas_width()//3+100,get_canvas_height()//4+70,200,50
    btn = Button("",l,b,w,h,font,"End", lambda: End())
    gfw.world.add(gfw.layer.menu, btn)

    l,b,w,h = get_canvas_width()//3+100,get_canvas_height()//4+130,200,50
    btn = Button("",l,b,w,h,font,"Continue", lambda: kontinue())
    gfw.world.add(gfw.layer.menu, btn)

def kontinue():
    global paused,open
    paused = False
    open = False
    for menu in gfw.world.objects_at(gfw.layer.menu):
        gfw.world.remove(menu)

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

    if player.handle_event(e):
        return
    if handle_mouse(e):
        return

capture = None
def handle_mouse(e):
    global capture
    if capture is not None:
        holding = capture.handle_event(e)
        if not holding:
            capture = None
        return True

    if open:
        for ui in range(gfw.layer.ui, gfw.layer.menu + 1):
            for obj in gfw.world.objects_at(ui):
                if obj.handle_event(e):
                    capture = obj
                    return True
    else:
        for obj in gfw.world.objects_at(gfw.layer.ui):
            if obj.handle_event(e):
                capture = obj
                return True


    return False

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