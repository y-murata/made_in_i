#coding:utf-8
import random as R
a=list(u'進捗どうですか');s=a[-5:]+a[:2];c=0
while a!=s:R.shuffle(s);c+=1;print' '.join(s),
print'?'*5
print c