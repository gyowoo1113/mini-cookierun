import gfw
import main_state

gfw.run(main_state)

# 1. running stage 좌표지정 완료
# 2. 체력바 구현
# 3. state push/pop 정리하기

# Boss(chaser) -> attack 제외하곤 충돌체크 하지않음
# -> attack 이후 충돌상태 아닐때까지 attack 마지막 image에서 멈춰있음
# -> 일어날때 좀 늦게 일어나게 해야함 -> FPS 건드리는 것보다 FIDX 건드리는게 나을듯
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

# ** player -> jump,magnet,biggest time 재는 cnt 변수를 공유하고 있음
# ** 오류 생기지 않는지 체크 후 수정필요