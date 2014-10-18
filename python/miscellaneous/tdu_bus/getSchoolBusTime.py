# -*- coding: utf-8 -*-
import time, urllib2, httplib, re

url = 'https://www.cse.dendai.ac.jp/campus/access/bus_school.html'


def getBusTimetable(html):  # 全体のバス時刻表(5種類:平日の大学行,平日の大学発,土曜,休業中平日,土曜日(8月))を取得
    timetables = re.compile('<div class="tableDefault">[\d\D]+?</table>').findall(html)
    return timetables


def getBusComeTime_01(timetable, name):
    tableDic = {}
    tableDic['tableName'] = name

    # 1時間ごとに区切る
    times = re.compile('<tr>[\d\D]+?</tr>').findall(timetable)

    # バスの種類
    tableType = re.sub('<[^>]*?>', '', times.pop(0)).strip()
    tableDic['busType'] = tableType

    # バスがどこからでるのかorどこにいくのか
    route = re.sub('<[^>]*?>', '', times.pop(0)).strip().split(u'\r\n')

    # 作業用2次元リスト
    dump = [[] for i in range(len(route))]

    for time in times:
        time = time.replace(u'<tr>', '').replace(u'</tr>', '').split(u'\r\n')
        while 0 < time.count(''):
            time.remove('')

        # 時間をpop
        hour = time.pop(0).replace(u'<th>', '').replace(u'</th>', '')

        # 出発地別に見る
        for index in range(len(time)):
            if time[index] != u'<td></td>':
                minute = time[index].replace(u'<td>', '').replace(u'</td>', '')
                minute = minute.split(u',')
                if type(minute) == list:
                    for jndex in range(len(minute)):
                        minute[jndex] = u':'.join((hour, minute[jndex]))
                else:
                    minute = u':'.join((hour, minute))
                dump[index].extend(minute)
    for i in range(len(route)):
        tableDic[route[i]] = dump[i]
    '''
    for i, j in enumerate(dump):
        tableDic[route[i]] = map(str, j)
        print(route[i])
        print(tableDic[route[i]])
    '''
    return tableDic


def getBusComeTime_234(timetable, name):
    tableDic = {}
    tableDic['tableName'] = name

    # 1時間ごとに区切る
    times = re.compile('<tr>[\d\D]+?</tr>').findall(timetable)

    # バスの種類
    tableType = re.sub('<[^>]*?>', '', times.pop(0)).strip().split(u'\r\n')
    tableDic['busType'] = tableType

    # バスがどこからでるのかorどこにいくのか
    route = re.sub('<[^>]*?>', '', times.pop(0)).strip().split(u'\r\n')
    route.remove('')

    # 作業用2次元リスト
    dump = [[] for i in range(len(route))]

    for time in times:
        time = time.replace(u'<tr>', '').replace(u'</tr>', '').split(u'\r\n')
        while time.count('') != 0:
            time.remove('')

        # 時刻を取得
        hour = time.pop(0)  # 時刻をpop
        time.remove(hour)  # 複数個あるので削除
        hour = hour.replace(u'<th>', '').replace(u'</th>', '')

        # 例外処理
        if len(time) == 7:
            time.pop(5)

        # 出発地別に見る
        for index in range(len(time)):
            if time[index] != u'<td></td>':
                minute = time[index].replace(u'<td>', '').replace(u'</td>', '')
                minute = minute.split(u',')
                if type(minute) == list:
                    for jndex in range(len(minute)):
                        minute[jndex] = u':'.join((hour, minute[jndex]))
                else:
                    minute = u':'.join((hour, minute))
                dump[index].extend(minute)
    for i in range(len(route)):
        tableDic[route[i]] = dump[i]
    '''
    for i, j in enumerate(dump):
        tableDic[route[i]] = map(str, j)
        print(route[i])
        print(tableDic[route[i]])
    '''
    return tableDic


# HTMLを取得する
def gethtml(url):  # URL文字列を引数にして，HTMLを取得して返す関数
    time.sleep(1)  # アクセス制限対策として引数秒待機する(ミリ秒ではない)
    try:
        return urllib2.urlopen(url).read()
    except httplib.BadStatusLine:  # エラーコードが現れたら
        time.sleep(10)  # 10秒待機
        return gethtml(url)  # 再帰する


def syori():
    html = unicode(gethtml(url), 'shift_jis')
    html = html.replace(u'	', '')
    html = html.replace(u'<sup>*</sup>', '')
    html = html.replace(u'&nbsp;', '')
    html = html.replace(u'　', ',')
    html = html.replace(u'<p>', '')
    html = html.replace(u'</p>', '')

    timetable = getBusTimetable(html)
    namelits = [u'講義期間中大学行平日', u'講義期間中大学発平日', u'講義期間中土曜', u'休業中平日', u'休業中土曜']
    dics = []
    dics.append(getBusComeTime_01(timetable[0], namelits[0]))  # 講義期間中大学行平日
    dics.append(getBusComeTime_01(timetable[1], namelits[1]))  # 講義期間中大学発平日
    dics.append(getBusComeTime_234(timetable[2], namelits[2]))  # 講義期間中土曜
    dics.append(getBusComeTime_234(timetable[3], namelits[3]))  # 休業中平日
    dics.append(getBusComeTime_234(timetable[4], namelits[4]))  # 休業中土曜

    import json, codecs
    # JSONファイル書き込み

    for i, dic in enumerate(dics):
        f = codecs.open('.'.join((namelits[i], 'json')), 'w', 'utf-8')
        json.dump(dic, f, sort_keys=True, indent=4, ensure_ascii=False)


if __name__ == '__main__':
    syori()
    pass