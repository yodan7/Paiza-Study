import pytest


input1 = """
3 5 1
L
""".strip()

output1 = """
2 5
""".strip()

input2 = """
-18 45 6
L
L
R
R
L
R
""".strip()

output2 = """
-19 45
-19 46
-20 46
-20 45
-21 45
-21 44
""".strip()


def main():
    x, y, n = map(int, input().split())
    moves = [input() for _ in range(n)]
    # board = [list(100) for _ in range(100)]
    point = [y, x]
    front = [y-1, x]

    for m in moves:
        diff = [b - a for a, b in zip(point , front)]
        if diff == [-1, 0]:
            d_right = [0, 1]
            d_left =  [0, -1]
        elif diff == [1, 0]:
                d_right = [0, -1]
                d_left = [0, 1]
        elif diff == [0, -1]:
                d_right = [-1, 0]
                d_left = [1, 0]
        elif diff == [0, 1]:
                d_right = [1, 0]
                d_left = [-1, 0]
        
        right = [p + q for p, q in zip(point , d_right)]
        left = [p + q for p, q in zip(point , d_left)]
        if m == "R":
            point = right
            front = [t + s for t, s in zip(point , d_right)]
        else:
            point = left
            front = [t + s for t, s in zip(point , d_left)]
        print(" ".join(map(str, reversed(point)))) 



# 開始時点の x , y 座標、移動の回数 N が与えられます。
# 続くN行で移動の向き d1 ... dN が与えられるので、与えられた順に移動をしたときの各移動後の x , y 座標 を答えてください。
# 移動者ははじめ北を向いています。

# なお、マスの座標系は下方向が y 座標の正の向き、右方向が x 座標の正の向きとします。

# ・ 移動をするごとに向く方角が変わること
# ・ 移動前に向いている方角によって同じ移動の向きでも座標の変化が違うこと
# の 2 点に気をつけてください。      
            


# 解答
x, y, n = map(int, input().split())
directions = ["N", "E", "S", "W"]
now_direction = 0

for _ in range(n):
    lr = input()
    if lr == "L":
        now_direction = (3 + now_direction) % 4
    else:
        now_direction = (1 + now_direction) % 4

    if directions[now_direction] == "N":
        y -= 1
    elif directions[now_direction] == "E":
        x += 1
    elif directions[now_direction] == "S":
        y += 1
    elif directions[now_direction] == "W":
        x -= 1

    print(x, y)
            
            




# 以下は固定
def test_main(monkeypatch) -> None:
    check(monkeypatch, main, input1, output1)
    check(monkeypatch, main, input2, output2)


def check(monkeypatch, func: None, input: str, output: str) -> None:
    import io

    stdin = io.StringIO(input)
    stdout = io.StringIO()

    with monkeypatch.context() as m:
        m.setattr("sys.stdin", stdin)
        m.setattr("sys.stdout", stdout)
        func()

    assert stdout.getvalue() == output + "\n"


if __name__ == "__main__":
    pytest.main([__file__])
