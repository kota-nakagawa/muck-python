# -*- coding: utf-8 -*-
#!/usr/bin/env

text = input('年齢は？')
age = int(text)  #int関数は引数に入力した文字列を整数化します#
if age<20:
    print('未成年')
else:
    print('成人')
