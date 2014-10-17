import java.time.Duration;
import java.time.ZoneId;
import java.time.ZonedDateTime;

//http://www.coppermine.jp/docs/programming/2014/07/date-and-time-api-5.html
//http://dev.ariel-networks.com/wp/archives/4186

public class WorkingEveryDay {
    public static void main(String args[]) {
        //タイムゾーンを日本に設定
        ZoneId jst = ZoneId.of("Asia/Tokyo");
        //今の時刻を取得
        ZonedDateTime today = ZonedDateTime.now(jst);
        //明日の12時を取得
        ZonedDateTime tomorrow = ZonedDateTime.now(jst).plusDays(1);//日を加算
        tomorrow = tomorrow.withHour(12);//時を設定(2桁)
        tomorrow = tomorrow.withMinute(00);//分を設定(2桁)
        tomorrow = tomorrow.withSecond(00);//秒を設定(2桁)
        tomorrow = tomorrow.withNano(000000000);//ナノ秒を設定(8桁)

        //今から設定した時刻まで何ミリ病あるのか
        Duration duration = Duration.between(today, tomorrow);
        long sleeptime = duration.toMillis();//待機するミリ秒

        //今の時刻を表示
        System.out.println("今の時刻は -> "+today);
        //設定した時刻の表示
        System.out.println("指定時刻は -> "+tomorrow);
        //設定した時刻までThread.sleep()で眠っているミリ秒数
        System.out.println("何ミリ秒寝てればいいの？ -> "+sleeptime);
    }
}
