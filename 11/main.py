import pico2d
import play_state
import logo_state

pico2d.open_canvas()

states = [logo_state, play_state] # 이 방법을 쓰면 게임 시작이나 정지, 또는 특정 화면으로 돌아가기 불가능
for state in states:
    state.enter()
    while state.running:
        state.handle_events()
        state.update() # 업데이트
        state.draw() # 화면 출력
    state.exit()

# start_state = logo_state # 모듈(소스코드) 자체를 변수화
# start_state.enter() # 대학 로고 출력 초기화
# # 게임 루프 도는 중
# while start_state.running:
#     start_state.handle_events()
#     start_state.update() # 업데이트
#     start_state.draw() # 산기대 화면 출력
#
# start_state.exit() # 대학 로고 출력 종료
#
# start_state = play_state # 모듈(소스코드) 자체를 변수화
# start_state.enter() # 메인 게임 초기화
# while start_state.running:
#     start_state.handle_events()
#     start_state.update()  # 업데이트
#     start_state.draw()  # 소년, 잔디 그리기
#     pico2d.delay(0.05)
# start_state.exit() # 메인 게임 종료

pico2d.close_canvas()