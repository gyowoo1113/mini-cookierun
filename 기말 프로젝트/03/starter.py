import gfw
import main_state

gfw.run(main_state)

# 1. running stage 좌표지정 완료

# Boss(another) -> 화면앞에서 알짱거림
# -> 앞의 장애물을 공격해서 캐릭터를 향해 던짐
# -> 장애물 만들어서 던짐
# -> object move_to_pos(0,player.pos(y))
# -> 단 crash와 별도의 변수를 둬야함 (헷갈림)

# 젤리 기능추가:
# 체력회복: 장애물 구현 후
# -> 크기젤리처럼 서서히 체력증가 하는걸 보여줘야함
# 보너스: 에디터 제작 후

# 화면밖에 벗어났을 때 꼭대기에서 리젠되는 방식이 아니라,
# 무적상태를 받아 서서히 올라온 후 떨어지도록 수정
# cookie 충돌박스 수정하기 -> get_bb에 각각 -10,+10 ... 해서 박스크기 줄이기

# ** player -> jump,magnet,biggest time 재는 cnt 변수를 공유하고 있음
# ** 오류 생기지 않는지 체크 후 수정필요