#import os
#os.chdir('C:/Users/LG/Desktop/플밍과제/2d겜플/res')
#os.getcwd()
#os.listdir()
from pico2d import *
open_canvas()
image = load_image('../res/character.png')
for x in range(0,9):
	for y in range(0,7):
		image.draw_now(x * 100, y * 100)
clear_canvas_now()
grass = load_image('../res/grass.png')
character = load_image('../res/character.png')

for s in range(100,300):
    clear_canvas_now()
    for y in range(100,501,100):
        for x in range(s,800,100):
            character.draw_now(x,y)

close_canvas()


