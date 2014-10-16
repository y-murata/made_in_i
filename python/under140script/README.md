#実行環境
Python 2.7.7 |Anaconda 2.0.1 (x86_64)|

#プログラム
    #coding:utf-8
    import random as R
    a=list(u'進捗どうですか')
    s=a[-5:]+a[:2]
    while a!=s:
    	R.shuffle(s)
    	for i in s:print i,
    print '?'*5

  
#参考サイト
[「進捗・どう・です・か」をランダムに表示し「進捗どうですか」が完成したら煽ってくるプログラム](http://elephnote.com/blog/archives/936 "「進捗・どう・です・か」をランダムに表示し「進捗どうですか」が完成したら煽ってくるプログラム")

[進捗プログラム]:http://elephnote.com/blog/archives/936 "「進捗・どう・です・か」をランダムに表示し「進捗どうですか」が完成したら煽ってくるプログラム"