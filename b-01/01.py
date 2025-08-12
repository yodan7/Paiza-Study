# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
input_nhw = input()
n, h, w = map(lambda x:int(x), input_nhw.split())

input_self = input()
x, y = map(lambda x:int(x), input_self.split())

input_move = input()

board = []
for i in range(h):
    lst = list(map(lambda x:int(x), input().split()))
    board.append(lst)



moveLst = [[-1, 0], [1, 0], [0, 1], [0, -1]]#前後左右
s = "FBRL"#サンプル文字列
p, q = x-1, y-1#現在の添え字
    
for j in range(0, n):
    move = input_move[j]#1つづつの文字列

    m = s.index(move)#サンプル文字を示す添え字
    p, q = [a+b for a, b in zip([p, q], moveLst[m])]#moveListの重みを現在の添え字に足す

    print(board[p][q])
    
        




