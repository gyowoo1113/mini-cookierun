import gfw
import gobj
import jelly

def check_items(player):
    for item in gfw.world.objects_at(gfw.layer.item):
        if gobj.collides_box(player, item):
            gfw.world.remove(item)
            check_jellys(player,item)
            break

def check_jellys(player,item):
    if item.type == 'jelly':
        player.score += 150
#    elif time.type == 'biggest':
#        pass    #커지는 젤리
#    elif time.type == 'magnet':
#        pass    #자석젤리