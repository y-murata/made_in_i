package lastExam;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.LinkedList;


public class LastExam extends JFrame {
    LinkedList<signboard> schedule = new LinkedList<>();//自作クラスを納めるリスト
    private JButton addBtn;//予定の追加ボタン
    private JScrollPane cntScrollPane = null;//スクロールパネル
    private JPanel tmpPane = null;//スクロールパネルに乗っかるダミーパネル

    //コンストラクタ
    LastExam(String title) {
        setTitle(title);//フレームタイトルを設定
        setSize(400, 600);//フレームサイズを設定
        //フレームのバツボタンで終了させる
        setDefaultCloseOperation(WindowConstants.EXIT_ON_CLOSE);

        //装飾を担う関数を呼ぶ
        arrange();
        //アクションリスナーの設定を担う関数を呼ぶ
        addActionListener();
        //再描画する関数をよぶ
        reSche();
    }

    private void arrange() {
        //パネルのレイアウトをボーダーレイアウトに設定
        setLayout(new BorderLayout());

        //JPanelの装飾を行う関数を呼ぶ
        arrangePane();
        //JButtonの装飾を行う関数を呼ぶ
        arrangeBtn();
    }

    private void arrangePane() {
        //スクロールパネルが設置されているならば撤去する
        if (cntScrollPane != null)
            remove(cntScrollPane);

        //スクロールパネルに乗っかるダミーパネルを生成
        tmpPane = new JPanel();
        //行が増えるようなボックスレイアウトに設定
        tmpPane.setLayout(new BoxLayout(tmpPane, BoxLayout.Y_AXIS));

        //スクロールパネルを生成
        cntScrollPane = new JScrollPane(tmpPane);
        //縦方向のスクロールは必要になったら表示
        //横方向のスクロールは出さない
        cntScrollPane.setVerticalScrollBarPolicy(JScrollPane.VERTICAL_SCROLLBAR_AS_NEEDED);
        cntScrollPane.setHorizontalScrollBarPolicy(JScrollPane.HORIZONTAL_SCROLLBAR_NEVER);
        //スクロールパネルをフレームの中央に配置
        add(cntScrollPane, BorderLayout.CENTER);

    }

    private void arrangeBtn() {
        //ボタンを生成
        addBtn = new JButton("予定を追加");
        //ボタンを下側に設置
        add(addBtn, BorderLayout.SOUTH);
    }

    //アクションリスナーを追加する関数
    private void addActionListener() {
        //予定追加ボタンにアクションリスナーを設定
        addBtn.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                //予定の入力を促す
                String value = JOptionPane.showInputDialog(null, "予定を入力してください", "予定");

                if (value != null) {//予定が入力されたならば
                    //スケジュールリストに看板を追加
                    schedule.add(new signboard(schedule.size(), value));
                    //再描画する関数をよぶ
                    reSche();
                }

            }
        });

    }

    //再描画を行う関数
    private void reSche() {
        //パネルの初期化を行う
        arrangePane();

        if (0 < schedule.size()) {//予定が1件でもあるならば
            signboard tmpBoard;//forループ内で使う看板の変数
            int index = 0;//配置した看板の数を記憶する変数
            for (; index < schedule.size(); index++) {
                tmpBoard = schedule.get(index);//看板リストから看板を先頭から取得
                tmpBoard.setId(index);//看板のIDをセットし直す
                schedule.set(index, tmpBoard);//看板リストにインデックスを指定して収納
                tmpPane.add(schedule.get(index));//看板が載るパネルに追加する
            }
            //もしも載る看板が5枚以下ならば空のパネルを貼付ける
            while (index < 5) {
                //空のパネルを生成
                JPanel nullPane = new JPanel();
                //空のパネルの大きさを指定
                nullPane.setPreferredSize(new Dimension(400, 100));
                //空のパネルを追加
                tmpPane.add(nullPane);
                index++;//インデックスを増やす
            }
        } else {//予定が無ければ
            //縦書きのラベルを作成
            JLabel label = new JLabel("<html>予<br/>定<br/>は<br/>あ<br/>り<br/>ま<br/>せ<br/>ん<br/>");
            //中央に文字が来るように設定
            label.setHorizontalAlignment(SwingConstants.CENTER);
            //ラベルのフォントや文字サイズを指定
            label.setFont(new Font(Font.SANS_SERIF, Font.PLAIN, 50));
            //パネルに設置
            tmpPane.add(label);
        }
        //scrollpaneの再描画命令を出す
        revalidate();
    }

    //看板パネルクラス
    private class signboard extends JPanel {
        private int id;//看板ID
        private JButton dltBtn;//看板を削除するボタン
        private JLabel content;//看板に示されている予定

        signboard(int id, String content) {
            //看板パネルの大きさを指定
            setPreferredSize(new Dimension(400, 100));

            this.id = id;//看板IDを取得

            this.content = new JLabel(content);//看板に書かれる文字列からラベルを生成
            this.content.setSize(300, 100);//ラベルのサイズを指定
            //ラベルのフォントや文字サイズを指定
            this.content.setFont(new Font(Font.SANS_SERIF, Font.PLAIN, 25));

            //看板パネル全体のアレンジを行う関数を呼ぶ
            arrange();
            //アクションリスナーを追加する関数を呼ぶ
            addActionListener();

        }

        //看板IDを再度設定する時に用いる関数
        void setId(int id) {
            this.id = id;
        }

        //看板パネル全体のアレンジを行う
        private void arrange() {
            //装飾を行う関数を呼ぶ
            arrangePane();
            //ボタンを設置する関数を呼ぶ
            arrangeBtn();
        }

        //このパネルの装飾を行う
        private void arrangePane() {
            //背景をグレーに設定する
            setBackground(new Color(200, 200, 200));
            //パネルのレイアウトをボーダーレイアウトに設定
            setLayout(new BorderLayout());
            //看板に表示される文字列を中央に配置
            add(content, BorderLayout.CENTER);
        }

        //このパネルに載るボタンの装飾を行う
        private void arrangeBtn() {
            dltBtn = new JButton("削除");//ボタンの生成
            dltBtn.setSize(100, 100);//ボタンの大きさを設定
            add(dltBtn, BorderLayout.WEST);//パネルの左側に設置
        }

        //アクションリスナーを追加する関数
        private void addActionListener() {
            //削除ボタンにアクションリスナーを追加する
            dltBtn.addActionListener(new ActionListener() {
                public void actionPerformed(ActionEvent e) {
                    //スケジュールリストから指定idの看板を削除
                    schedule.remove(id);
                    //再描画を行う関数を呼ぶ
                    reSche();
                }
            });

        }
    }


    public static void main(String[] args) {
        new LastExam("to do").setVisible(true);
    }
}
