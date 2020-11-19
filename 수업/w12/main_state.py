from  pico2d import *
import gfw
import player
import generator
import bg

def collides_distance(a,b):
    ax,ay = a.pos
    bx,by = b.pos
    distance_sq = (ax-bx)**2 + (ay-by)**2
    radius_sum = a.radius + b.radius
    return distance_sq < radius_sum**2

def check_collision():
    for m in gfw.world.objects_at(gfw.layer.missile):
        if collides_distance(player,m):
            gfw.world.remove(m)

def enter():
    gfw.world.init(['bg','missile','player'])
    generator.init()

    bg.init(player)
    gfw.world.add(gfw.layer.bg,bg)
    player.init()
    gfw.world.add(gfw.layer.player,player)

def exit():
    pass
def update():
    gfw.world.update()
    generator.update()
    check_collision()
def draw():
    gfw.world.draw()
def handle_event(e):
    if e.type == SDL_QUIT:
        gfw.quit()
    if e.type == SDL_KEYDOWN:
        if e.key == SDLK_ESCAPE:
            gfw.pop()

    player.handle_event(e)

if __name__ == '__main__':
    gfw.run_main()