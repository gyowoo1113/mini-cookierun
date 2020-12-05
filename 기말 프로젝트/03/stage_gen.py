import gfw
from pico2d import *
from flatform import Platform
from jelly import Jelly
import gobj
from player import Player
from factory import Factory
from boss import Boss

UNIT_PER_LINE = 100
SCREEN_LINES = 10
BLOCK_SIZE = 60

factory = None
lines = []

def load(file):
    global factory,File
    if factory is None:
        factory = Factory()
    File = file

    global lines, current_x, create_at, map_index
    with open(file, 'r') as f:
        lines = f.readlines()
    current_x = 0
    map_index = 0
    create_at = get_canvas_width() + 2 * BLOCK_SIZE

ignore_char_map = set()
def count():
    return len(lines) // SCREEN_LINES * UNIT_PER_LINE

def update(dx):
    global current_x, create_at
    current_x += dx
    while current_x < create_at:
        create_column()


def create_column():
    global current_x, map_index
    y = BLOCK_SIZE  // 2
    for row in range(SCREEN_LINES):
        ch = get(map_index, row)
        create_object(ch, current_x, y)
        y += BLOCK_SIZE
    current_x += BLOCK_SIZE
    map_index += 1
    #print('map_index:', map_index)

def create_object(ch, x, y):
    if ch in ['1','2','3','4','5','6']:
        obj = Jelly(ord(ch) - ord('1'), x, y)
        gfw.world.add(gfw.layer.item, obj)
        #print('creating Jelly', x, y)
    elif ch in ['O','P']:
        dy = 1 if ch == 'O' else 3 #4
        y -= dy * BLOCK_SIZE // 2
        x -= BLOCK_SIZE // 2
        obj = Platform(ord(ch) - ord('O'), x, y)
        gfw.world.add(gfw.layer.platform, obj)
        #print('creating Platform', x, y)
    elif ch in ['B']:
       e = Boss(x,y-10)
       gfw.world.add(gfw.layer.boss, e)
    else:
        if ch == 'X':
            y-= 105
        elif ch == 'Y':
            y-= 33
        elif ch == 'Z':
            y+= 10
        ao = factory.create(ch, x, y)
        if ao is None:
            global ignore_char_map
            if ch not in ignore_char_map:
                print("Error? I don't know about: '%s'" % ch)
                ignore_char_map |= {ch}
            return
        l,b,r,t = ao.get_bb()
        ao.pass_wh(r-l, t-b)
        gfw.world.add(gfw.layer.enemy, ao)

def get(x, y):
    col = x % UNIT_PER_LINE
    row = x // UNIT_PER_LINE * SCREEN_LINES + SCREEN_LINES - 1 - y
    if row > len(lines):
        load(File)
    else:
        return lines[row][col]
