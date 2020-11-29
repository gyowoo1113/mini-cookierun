import gfw
import main_state

gfw.run(main_state)

# title_state, ready_state ui 제작
# 사운드 넣어야함 -> ui 클릭 사운드
# button text 정리
# ready_state player 고르기(open)추가

# Boss(another) -> 화면앞에서 알짱거림
# -> 앞의 장애물을 공격해서 캐릭터를 향해 던짐
# -> 장애물 만들어서 던짐
# -> object move_to_pos(0,player.pos(y))
# -> 단 crash와 별도의 변수를 둬야함 (헷갈림)

# 젤리 기능추가:
# 보너스: 에디터 제작 후

# 화면밖에 벗어났을 때 꼭대기에서 리젠되는 방식이 아니라,
# 무적상태를 받아 서서히 올라온 후 떨어지도록 수정