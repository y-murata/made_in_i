#coding:utf-8
import random as R
a=list(u'進捗どうですか');s=a[-5:]+a[:2]
while a!=s:R.shuffle(s);print' '.join(s),
print'?'*5