<?php
/**
 * 2次元の連想配列をcsv形式で書き出す
 *
 * @todo ：書き出されたファイルの文字コードはutf8なのでエクセルで開きたい場合，SJISやBOM付きUTF8に変換する必要がある
 *      
 * @param String $fileName
 *        	書き出し先ファイル名
 * @param 2DAssociationArray $arg2dList
 *        	書き出したい2次元連想配列
 * @param Array $assocOrderKeys
 *        	書き込む順番を決定する連想配列の第一keyを格納した配列
 */
function save_2d_assocarray($fileName, $arg2dList, $assocOrderKeys) {
	$time_start = microtime ( true );
	
	// タイムゾーンを日本時間に設定
	$org_timezone = date_default_timezone_get ();
	date_default_timezone_set ( 'Asia/Tokyo' );
	
	echo 'a';
	
	$fp = fopen ( date ( 'YmdHi' ) . $fileName, 'w' );
	foreach ( $assocOrderKeys as $firstkey ) {
		foreach ( $arg2dList [$firstkey] as $secondkey => $val ) {
			echo $firstkey . ',' . $secondkey . ',' . $val . '<BR>';
			$putary = [ 
					$firstkey,
					$secondkey,
					$val 
			];
			if (fputcsv ( $fp, $putary, ',', '"' ) == 0) {
				echo 'Doubtful data(' . $firstkey . ', ' . $secondkey . ', ' . $val . '): see FILE(' . $filename . ') with own eyes.';
			}
		}
	}
	fclose ( $fp );
	
	// タイムゾーンを元に戻す
	date_default_timezone_set ( $org_timezone );
	
	$time = microtime ( true ) - $time_start;
	echo 'save_2d_assocarray : ' . $time . '秒';
}

$filename = 'savedata.csv';
$arg2dList = [ 
		'gender' => [ 
				'male' => 111,
				'feale' => 222 
		],
		'ageband' => [ 
				'teenage' => 11,
				'twenties' => 22,
				'thirties' => 33,
				'forties' => 44,
				'fifties' => 55,
				'sixties' => 66,
				'over-sixties' => 77 
		] 
];
$assocOrderKeys = [ 
		'gender',
		'ageband' 
];
save_2d_assocarray ( $filename, $arg2dList, $assocOrderKeys );
?>
