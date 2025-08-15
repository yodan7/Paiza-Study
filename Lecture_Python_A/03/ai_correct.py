h, w, sy, sx, n = map(int, input().split())
# 各要素の文字列を文字ごとに分け、2次元配列化
s = [[p for p in input()] for _ in range(h)]
# rotate = {}
# for _ in range(n):
#     k, v = input().split(" ")
#     rotate[k] = v

rotate = [input().split(" ") for _ in range(n)]

# N, E, S, W
dy = [-1, 0, 1, 0]
# N, E, S, W
dx = [0, 1, 0, -1]
now_direction = 0 # 0, 1, 2, 3

# h, w, ... の入力部分は省略

# dx, dy, now_direction の定義は同じ

# ★★★ 改善点1: 開始地点はループの前にマークする ★★★
s[sy][sx] = "*"
y, x = sy, sx

# ★★★ 改善点2: forループで時間を管理する ★★★
for t in range(100):
    # 方向転換のチェック (ここはあなたのロジックのままでもOK)
    if rotate and t == int(rotate[0][0]):
        lr = rotate.pop(0)[1] # .pop(0)の方が少し効率的
        if lr == "L":
            now_direction = (now_direction + 3) % 4
        else:
            now_direction = (now_direction + 1) % 4
    
    # ★★★ 改善点3: 次の座標を「一時変数」に計算する ★★★
    ny = y + dy[now_direction]
    nx = x + dx[now_direction]
    
    # ★★★ 改善点4: 「一時変数」を検証する ★★★
    if not (0 <= ny < h and 0 <= nx < w and s[ny][nx] == "."):
        # 進めないならループを抜ける
        break
    
    # ★★★ 改善点5: 検証OKなら、座標を更新してマークする ★★★
    y, x = ny, nx
    s[y][x] = "*"

# 出力部分は同じ

for row in ["".join(cell) for cell in s]:
    print(row)

# print(s)
# print(h, w, sy, sx, n)