import gfw
import main_state

gfw.run(main_state)

# doublejump 수정해야함 (프레임 타이밍 안맞는 문제)
# -> 좀더 깔끔하게 애니메이션 동작하길 원함
#   a. 발판에 도달했을때 착지 action 취하기
#   b. doublejump action 한번 수행 후 falling으로 전환
# cookie size문제 해결하기 -> 통일하기
# state & action 동시에 사용하고 있는 부분 수정필요
#   action 으로만 애니메이션 조절 가능한지 테스트
# 발판 좌표위치 지정해야함 (json)
# 이번주 내로 에디터 만들기
#   주말전까지 젤리 & 발판 만들어서 주말에 좌표지정 하기
