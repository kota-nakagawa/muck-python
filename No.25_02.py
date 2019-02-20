# -*- coding: utf-8 -*-
#!/usr/bin/env

'''入力した税抜金額を入力したら税込金額を出すようなプログラムを完成させなさい'''

print("計算したい金額を入力してください")
number = int(input())
tax = 0.08
sum = int(round((number * tax)+number))
print("税込み金額は"+str(sum)+"円です")