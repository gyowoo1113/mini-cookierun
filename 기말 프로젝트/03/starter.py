import gfw
import main_state

gfw.run(main_state)

# 계속 달리고 있을때 플랫폼 없어도 안떨어지는 버그 수정
# 점프해서 플랫폼 착지할때 l,r 전부 플랫폼 안에 들어있어야만 착지하는것 수정
# jelly json으로 정리 가능한지 확인 후 수정
# title_state, ready_state ui 제작
# 사운드 넣어야함 -> boss sound
#              -> ui 클릭 사운드

# Boss(another) -> 화면앞에서 알짱거림
# -> 앞의 장애물을 공격해서 캐릭터를 향해 던짐
# -> 장애물 만들어서 던짐
# -> object move_to_pos(0,player.pos(y))
# -> 단 crash와 별도의 변수를 둬야함 (헷갈림)

# 젤리 기능추가:
# 보스: 보스 존재할때 보스젤리 먹으면 점수가 크게증가
# 보너스: 에디터 제작 후

# 화면밖에 벗어났을 때 꼭대기에서 리젠되는 방식이 아니라,
# 무적상태를 받아 서서히 올라온 후 떨어지도록 수정