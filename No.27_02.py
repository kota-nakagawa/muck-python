#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ジョジョと入力したら「オラ」と１０回表示して、
# ディオと入力したら「無駄」と１０回表示し、
# それ以外の文字を入力したら「ゲームオーバー」と表示する。

jojo=input('ジョジョかディオと入力してください')
if jojo=='ジョジョ':
    for x in range(10):
        print('オラ')
elif jojo=='ディオ':
    for x in range(10):
        print('無駄')
else:
    print('ゲームオーバー')
