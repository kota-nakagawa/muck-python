# -*- coding: utf-8 -*-
#!/usr/bin/env

#変数pointが
#90以上ならExcellentと表示し、
#70以上ならGoodと表示し、
#50以上ならFairと表示し、
#それ以外ならBadを表示

your_point = input('点数を入力しなさい')
point = int(your_point)

if point > 49:
    if point >= 90:
        print('Excellent')
    elif point >= 70:
        print('Good')
    else:
        print('fair')
else:
    print('Bad')

#比較演算子

#  ==	a == b	bがaに等しい
#  !=	a != b	bがaに等しくない
#  >    a >  b	bよりaが大きい
#  >=	a >= b	bよりaが大きいか等しい
#  <	a <  b	bよりaが小さい
#  <=	a <= b	bよりaが小さいか等しい
#  in   a in b	BにAが含まれていれば真（これは少し特殊で、Bがリスト、Aが文字列、等の場合に使う)リスト、Aが文字列、等の場合に使う)
