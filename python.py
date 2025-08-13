# 最初の行で、続く入力の行数を取得
N = int(input())

# N回ループして、N個の整数を取得し、リストに格納
# int型の2次元配列作成
input_list = [int(input()) for _ in range(N)]

# input_listの中身の例: [10, 20, 30, ...]


# 1行の文字列を取得（例: "10 20 30"）
input_line = input().split()

# 各要素を整数に変換し、リストに格納
# input_listの中身の例: [10, 20, 30]
input_list = list(map(int, input_line))


#---------------
#辞書型のアプローチ
h, w = (2, 3)
maps = [list(input()) for _ in range(h)]
map_dict={}
for i in range(h):
    for j in range(w):
        if (i, j) in map_dict:
            continue
        map_dict[(i, j)] = 1 if maps[i][j] == "#" else 0


# --------上下左右の判
# is_top_ok = (y == 0) or (s[y - 1][x] == '#')


"""
(1) リスト操作
sort() / sorted(): リストの要素をソートする際に使います。

list.sort(): リスト自体を並び替えます。元のリストが変更されます。

sorted(list): 並び替えた新しいリストを返します。元のリストは変更されません。

reverse(): リストの要素を反転させます。

max() / min(): リストの最大値・最小値を取得します。

max([10, 20, 5]) -> 20

sum(): リストの合計値を計算します。

sum([10, 20, 5]) -> 35

(2) 文字列操作
split(): 文字列を指定した区切り文字で分割し、リストにします。

join(): 文字列のリストを指定した区切り文字で結合します。

" ".join(['Hello', 'World']) -> "Hello World"

strip(): 文字列の先頭と末尾にある空白文字を削除します。

len(): 文字列やリストの長さを取得します。
"""


# 向きの替え方
# NEWSのそれぞれを、dx, dyの値として捉えることでデータを簡略化
# 4方向の為 +1 や -3で表現し、%4で割って0-3までの4つの長さに集約する
"""
x, y, n = map(int, input().split())
#       N,  E,  S,  W (x座標の変化量)
dx = [  0,  1,  0, -1]
#       N,  E,  S,  W (y座標の変化量)
dy = [ -1,  0,  1,  0]

now_direction = 0 # 0:N, 1:E, 2:S, 3:W

for _ in range(n):
    lr = input()
    if lr == "L":
        now_direction = (now_direction + 3) % 4
    else:
        now_direction = (now_direction + 1) % 4
    
    # if文を使わずに、配列から直接変化量を取得
    x += dx[now_direction]
    y += dy[now_direction]

    print(x, y)
"""