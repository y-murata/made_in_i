#encoding:utf-8
#PILとかpillowとかlibjpegとかで怒られる場合，
#conda環境ではpipのPILをuninstallして，condaでpillowをinstallすると良い？
import qrcode as QR	#qrcodeのライブラリをインポート
img = QR.make('hello world')#QRコードの生成
img.show()#QRコードの表示
#なぜか表示してからでないとsaveがエラーを吐く
img.save('hello_world.png')#QRコードを保存する
