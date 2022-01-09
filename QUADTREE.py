# 쿼드 트리 뒤집기
# https://algospot.com/judge/problem/read/QUADTREE

C = int(input())

def reverse(s, i):
    if s[i] == 'b' or s[i] == 'w':
        return s[i]
    # x가 나온 경우
    i += 1
    upperLeft = reverse(s, i) # 왼쪽 위
    i += len(upperLeft)
    upperRight = reverse(s, i) # 오른쪽 위
    i += len(upperRight)
    lowerLeft = reverse(s, i) # 왼쪽 아래
    i += len(lowerLeft)
    lowerRight = reverse(s, i) # 오른쪽 아래
    return 'x' + lowerLeft + lowerRight + upperLeft + upperRight

for _ in range(C):
    compressed = input().rstrip()
    print(reverse(compressed, 0))