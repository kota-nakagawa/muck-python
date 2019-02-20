# -*- coding: utf-8 -*-
#!/usr/bin/env python

#for文の応用

import turtle
import random

# タートルを生成
my_turtle = turtle.Turtle()
# タートルの形を設定
my_turtle.shape("turtle")
# ペンの太さを設定
my_turtle.pensize(4)

# スクリーンを取得
screen = turtle.Screen()
# スクリーンのサイズを設定
screen.setup(800, 800)
screen.title("円を複数描く")

#6回繰り返して円を描く
for text in range(60):
    my_turtle.circle(100)
    my_turtle.left(15)

screen.mainloop()
