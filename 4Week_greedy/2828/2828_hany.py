# 2828번 사과 담기 게임
'''
스크린은 N칸으로 나누어져 있다. 스크린의 아래쪽에는 M칸을 차지하는 바구니가 있다. (M<N) 
레이어는 게임을 하는 중에 바구니를 왼쪽이나 오른쪽으로 이동할 수 있다.
하지만, 바구니는 스크린의 경계를 넘어가면 안 된다.

가장 처음에 바구니는 왼쪽 M칸을 차지하고 있다.

스크린의 위에서 사과 여러 개가 떨어진다.
각 사과는 N칸중 한 칸의 상단에서 떨어지기 시작하며, 스크린의 바닥에 닿을때까지 직선으로 떨어진다.

한 사과가 바닥에 닿는 즉시, 다른 사과가 떨어지기 시작한다.

바구니가 사과가 떨어지는 칸을 차지하고 있다면, 바구니는 그 사과가 바닥에 닿을 때, 사과를 담을 수 있다.
상근이는 사과를 모두 담으려고 한다.

이때, 바구니의 이동 거리의 최솟값을 구하는 프로그램을 작성하시오.
'''

# 최소값 구하기 -> 그리디 고려 가능 키워드

# 첫 시작은 무조건 1
# 바구니의 칸이 가용범위에 해당. 이 가용 범위가 칸 범위를 넘어서면 안된다.
# 1. 바구니가 사과 위치에 해당하면 움직이지 않는다. cnt += 0
# 2. 바구니가 사과 오른쪽에 위치하면 해당 사과가 있는 곳까지 cnt -= i
# 3. 바구니가 사과 왼쪽에 위치하면 해당 사과가 있는 곳까지 cnt += i
# 지금 당장 가장 최선의 선택을 한다.

n, m = map(int, input().split()) # n 칸, 왼쪽부터 m칸을 차지하는 바구니
j = int(input()) # 사과의 개수
cnt = 0 # 카운팅 초기값
cur = 1 # 시작은 무조건 1

for i in range(j):                     
    apple = int(input())
    # 범위 고려   
    # 바구니가 사과 위치를 포함하면? 
    # 움직이지 않아도 되므로 조건을 굳이 입력할 필요가 없다.                                
    if cur <= apple < cur + m: 
        continue

    # 바구니가 사과 왼쪽에 위치한다면? 해당 위치가 포함되는 칸만큼 전진
    elif cur < apple:
        cnt += apple - (cur + m - 1)
        cur = apple - m + 1

    # 바구니가 사과 오른쪽에 위치한다면? 후진
    elif cur > apple:   
        cnt += cur - apple
        cur = apple
print(cnt)