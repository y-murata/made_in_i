## ▼関連URL

* PR参考記事: [Pull Request のフォーマットを決めるとレビューの効率が3倍よくなる](http://engineering.crocos.jp/post/98455177675/pull-request-%E3%81%AE%E3%83%95%E3%82%A9%E3%83%BC%E3%83%9E%E3%83%83%E3%83%88%E3%82%92%E6%B1%BA%E3%82%81%E3%82%8B%E3%81%A8%E3%83%AC%E3%83%93%E3%83%A5%E3%83%BC%E3%81%AE%E5%8A%B9%E7%8E%87%E3%81%8C3%E5%80%8D%E3%82%88%E3%81%8F%E3%81%AA%E3%82%8B)
* 対応するtrello: https://trello.com/c/g8cD9awr
* 既存部分のテストケース作成に使ったスクリプト：https://github.com/oz-sysb/manual/pull/22
* 設計：https://github.com/oz-sysb/EasyAnalyticsPJ/blob/master/簡単集計PJ/設計/要件定義/20151214_簡単集計F2_会員属性情報をdeedeeで見れるようにする.md

## ▼ユーザストーリー
* < sp新規登録時に取得したユーザーの子供有無をdeedeeで更新したい >したい。<br />
なぜなら< リニューアル以降の属性別の利用状況を見れるようになる >ためだ。

## ▼概要
* SPリニューアル後、子供の有無と未既婚の情報が取得できるようになったが、取得した情報はdeedee/member_attributesに反映されていない
* 本修正により、deedee/member_attributesのカラム「children」「marriage」に正しい値が入ることになる。つまりは以下の様になる。
  * marriageが「未婚」ならば、未婚属性を付与する
    * marriage = 0
  * marriageが「既婚（子供なし）」ならば、既婚と子供なし属性を付与する
    * marriage = 1, children = 0
  * marriageが「既婚（子供あり）」ならば、既婚と子供あり属性を付与する
    * marriage = 1, children = 4


## ▼影響範囲・ターゲットユーザ

* 会員の属性情報に関わるところ全て
* 表への影響はない
* 2015/12/12,13のイベントで登録したユーザの属性がわかるようになる

## ▼技術的変更点概要

### todo
* [\aslan\applications\api\modules\batch\helpers\member_attribute_convert_helper.php](https://github.com/oz-sysb/aslan/blob/master/applications/api/modules/batch/helpers/member_attribute_convert_helper.php)
  * [x]  convert_attributes_data関数にデータを変換するメソッドを追加する

### 変更点
* converted_by_marriage_attributesメソッドを新規作成
* _convert_attributes_data_childrenメソッドに「子供あり」に対応するif文を追加
* convert_attributes_dataメソッドの機能を担保するユニットテストを作成

## ▼使い方

* 本番cronで実行されている: https://github.com/oz-sysb/hn-banana01/blob/master/batch/crontab#L253

* 起動コマンド
```
/usr/bin/php /var/www/xx-aslan/htdocs/index.php batch/member_attributes_register run
```
```
/usr/bin/php /var/www/xx-aslan/htdocs/index.php batch/member_attributes_update run
```

## ▼テスト結果とテスト項目

### convert_attributes_dataメソッドに対して
* 新規追加部分
- [x] segments_research_answersでmarriageに対する回答をしたユーザは、member_attributesのchildrenとmarriageに値が入る

|segments_research_answers/marriage|member_attributes/marriage|member_attributes/children|
|:--:|:--:|:--:|
|未婚|0||
|既婚(子供なし)|1|0|
|既婚(子供あり)|1|4|

* 既存部分

![image](https://cloud.githubusercontent.com/assets/10649624/11801070/9a4cb112-a325-11e5-95ea-cfa3953e9a74.png)

上記のパターンでpictmasterを使って組み合わせを出してユニットテストを作成した
組み合わせ生成は、関連のリンク[既存部分のテストケース作成に使ったスクリプト]を見てほしい

## ▼共有先

コードレビュー:

- [x] HipChat 簡単集計
- [x] HipChat 制作開発

社内共有:

- [ ] HipChat 簡単集計
- [ ] HipChat 制作開発

## ▼リリース物

* applications/api/modules/batch/helpers/member_attribute_convert_helper.php

## ▼その他

* 本修正の後の実行時での懸念：カラムの情報の方が正しい場合に、過去の値で塗り替えてしまうのではないか