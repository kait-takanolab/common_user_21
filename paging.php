<html>
<head>
    <title>画像データをページング</title>
</head>
<body>
	<h1>画像データをページング</h1>
    <?php

print ("Connecting to MySQL....<br>"); 


try { 
//データベースへのログイン
$pdo = new PDO('mysql:host=localhost;dbname=imagedb;charset=utf8','root','',array(PDO::ATTR_EMULATE_PREPARES => false)); 
} catch (PDOException $e) { 
//エラー処理
    exit('DB connection error.'.$e->getMessage()); 
}

$stmt = $pdo->query("SELECT * FROM images;");//画像データを表示するSQL文 

//-------------------------------------------------------




define('MAX','3');

$books = array(
          array('book_kind' => "ここは画像表示", "book_name" => "http://localhost/imagedb/test_00001.png"),
          array('book_kind' => "ここは画像表示", "book_name" => "http://localhost/imagedb/test_00002.png"),
          array('book_kind' => "ここは画像表示", "book_name" => "http://localhost/imagedb/test_00003.png"),
          array('book_kind' => "ここは画像表示", "book_name" => "http://localhost/imagedb/test_00004.png"),
          array('book_kind' => "ここは画像表示", "book_name" => "http://localhost/imagedb/test_00005.png"),
          array('book_kind' => "ここは画像表示", "book_name" => "http://localhost/imagedb/test_00006.png"),
            );

$books_num = count($books);
$max_page = ceil($books_num / MAX);

if(!isset($_GET['page_id'])){
    $now = 1;
}else{
    $now = $_GET['page_id'];
}

$start_no = ($now - 1) * MAX;

$disp_data = array_slice($books, $start_no, MAX, true);



//-----------------------------------------------------------
foreach($disp_data as $val){
 echo "{$val['book_kind']}　{$val['book_name']}<br />";

//画像として表示
print("<img src=\"".$val['book_name']." \" > "."<br>");

}

//}
//------------------------------------------------------

echo "全件数{$books_num}件　"; // 全データ数の表示です。

if($now > 1){ // リンクをつけるかの判定
    echo "<a href='paging.php?page_id=" . ($now - 1) . "'>前へ</a>" . '　';
} else {
    echo '前へ'. '　';
}

for($i = 1; $i <= $max_page; $i++){
    if ($i == $now) {
        echo $now. '　';
    } else {
        echo "<a href='paging.php?page_id=" . $i . "'>". $i. '</a>'. '　';
    }
}

if($now < $max_page){ // リンクをつけるかの判定
    echo "<a href='paging.php?page_id=".($now + 1). "'>次へ</a>". '　';
} else {
    echo '次へ';
}


//-------------------------------------------------------


?>
</body>
</html>