import gfw
import main_state

gfw.run(main_state)

# 1. running stage 좌표지정 완료
# 2. 체력바 구현

# 보완해야 하는 것
# 객체들 size조절
# 크기젤리 -> 장애물 파괴기능 추가
# 화면밖에 벗어났을 때 꼭대기에서 리젠되는 방식이 아니라,
# 무적상태를 받아 서서히 올라온 후 떨어지도록 수정

# 젤리 기능추가:
# 체력회복: 장애물 구현 후
# 보너스: 에디터 제작 후
# 보스: 장애물 구현 후
# 스피드: 구현미정( 시간 남았을때)

# ** player -> jump,magnet,biggest time 재는 cnt 변수를 공유하고 있음
# ** 오류 생기지 않는지 체크 후 수정필요