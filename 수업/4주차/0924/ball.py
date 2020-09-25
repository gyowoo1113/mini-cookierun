from pico2d import *
from gobj import *
import gfw_image

class Ball:
    balls = [] #<- class valuable, 클래스가 다같이씀, 클래스가 가지고 있는 변수
    def __init__(self, pos, delta, big=False):
        imageName = '/ball41x41.png' if big else '/ball21x21.png'
        self.image = gfw_image.load(RES_DIR + imageName)
        self.pos = pos                            # 객체마다 각자가 가지고 있는 멤버 변수-> member valuable
        self.delta = delta                        # ex) self.x : self의 member valuable
        self.radius = self.image.h // 2
        # print('Radius = %d' % self.radius)
    def draw(self):
        self.image.draw(*self.pos)
    def update(self):
        x,y = self.pos
        dx,dy = self.delta
        x += dx
        y += dy
        gravity = 0.1
        dy -= gravity

        bottom = y - self.radius        # 크기가 큰 공도 있기 때문에 중점 기준이 아닌 바닥 기준으로 잡아야함
        if bottom < 50 and dy < 0:      # 공이 내려가고 있는 동안에만 : dy<0
            dy *= rand(-0.8)            # 에너지 손실 발생 -> -1이 아니라 0.8
            if dy <= 1:                 # ㄴ자연스러움 위해서 rand -> 무조건 에너지 손실이 20% 일어나는 것이 아님
                dy = 0                  # 튀어오르는 양이 1이 안되면 0으로 하자

        if x < -100 or x > get_canvas_width() + 100:        # 중점이기 때문에 0,0이 아니라 -100,100으로 함
            Ball.balls.remove(self)                         # 화면 밖 벗어나면 삭제
            print('Ball count - %d' % len(Ball.balls))
            # balls에 대해서 루프를 돌고있음
            # -> 어떤 컬렉션에 대해 루프를 돌면서 컬렉션에 영향에 끼치는 일을 하면 안됨 (추가, 삭제하면 안됨)
            # 다른 언어에서 이렇게 사용하면 터질 수 있음 (루프 돌면서 추가, 삭제 등 영향 끼치는 일 하면 X)
            # 삭제할거 마킹 -> 루프 끝나고 마킹한거 삭제하는 식으로 해야함
        self.pos = x, y
        self.delta = dx, dy