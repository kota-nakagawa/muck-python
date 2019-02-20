# -*- coding: utf-8 -*-
#!/usr/bin/env

#変数ageが20歳未満なら未成年、
#変数ageが65歳未満なら高齢者、
#それ以外なら成人と表示する。

text = input('年齢は?')
age = int(text)
if age > 0:
    if age < 20:
        print('未成年')
    elif age >= 65:
        print('高齢者')
    else:
        print('成人')
else:
    print('正しく入力して下さい')

#最後に、次の記号を理解する。

#比較演算子

#  ==	a == b	bがaに等しい
#  !=	a != b	bがaに等しくない
#  >    a >  b	bよりaが大きい
#  >=	a >= b	bよりaが大きいか等しい
#  <	a <  b	bよりaが小さい
#  <=	a <= b	bよりaが小さいか等しい
#  in   a in b	BにAが含まれていれば真（これは少し特殊で、Bがリスト、Aが文字列、等の場合に使う)
