from pico2d import *
open_canvas()
character = load_image('../res/cookie/cookie02_run.png')
# 01 - 180,200  02 - 170,224  03-190,256
x=0
frame=0
while (x<800):
    clear_canvas()
    character.clip_draw(frame*170,0,170,224,x,180)
    update_canvas()
    frame = (frame+1)%3
    x+=5
    delay(0.05)
    get_events()

close_canvas()
