<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>哇哈哈哈哈哈</h1>
    <h2>哇哈哈哈哈哈</h2>
    <h3>哇哈哈哈哈哈</h3>
    <h4>哇哈哈哈哈哈</h4>
    <h5>哇哈哈哈哈哈</h5>
    <h6>哇哈哈哈哈哈</h6>
</body>
</html>
------------------------------------------------

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>哇哈哈哈哈哈</h1>
    <h2>哇哈哈哈哈哈</h2>
    <h3>哇哈哈哈哈哈</h3>
    <h4>哇哈哈哈哈哈</h4>
    <h5>哇哈哈哈哈哈</h5>
    <h6>哇哈哈哈哈哈</h6>
</body>
</html>
------------------------------------------------

<?php
    //注释：这是php结构
    #注释：单行注释
    /**
     * 多行注释：输出语句
    */

    echo 'hello';
    echo 'br/';
    echo 'world';
    echo '<h2>标题</h2>'

?>
------------------------------------------------

<?php
    #$str = 123;
    // $str = 'hello world';
    // echo $str;

    $str='hello';
    echo gettype($str);
    echo '<br/>';   #br/换行  hr横线

    $num = 100;
    echo gettype($num);
    echo '<br/>';
    
    $n = 10.2;
    echo gettype($n);
    echo '<hr/>';

    $flag = true;
    echo gettype($flag);
    echo '<hr/>';

    //字符串和js里面有什么不同:
    //1.js里面拼接 + 但是php用.  2.'' ""区别: ""解析变量 然后输出 '' 单引号直接输出内容
    $str = "hello world";
    echo $str;
    echo '$str';  #单引号是直接输出，双引号是解析内容再输出
    echo "$str";

    $eat = '今天中午吃什么？';
    $food = "吃烤羊肉";
    //echo "小明说:".$eat."我说:".$food;
    echo "小明说:$eat 我说: $food";  #""解析，空格隔开

?>
------------------------------------------------

<?php 
    //1.定义数组
    $arr = [10,20,30,'hello',true];
    //echo 数据简单的数据类型
    #echo $arr[0];
    #echo $arr[-1];
    
    //var_dump(变量) 数据类型
    //print_r(数组) 数组的输出方式

    var_dump($arr);   #位置 + 类别 + 内容
    echo '<hr/>';          #横线分割
    print_r($arr);    #输出数组
    //注意: php里面的数组和js里面不一样

    //2. $arr = array(key=>value,...)
    $arr2 = array('unname' => 'huahua','age' => 20,'sex' => 'nan');
    print_r($arr2);
    echo $arr2['sex'];
    echo '<hr/>';

    //3.$arr=[key=>value,...]
    $arr3 = ['yuwen'=>90,'yingyu'=>60];
    print_r($arr3);
    echo 'hr/';

    #4.遍历数组 foreach
    //语法：foreach(数组名字 as 每一项内容){}
    foreach ($arr2 as $item){
        echo $item;
    }
    
    echo 'hr/';

    //语法2: foreach(数组名字 as $key=>$value){}
    //$key 键名 可以任意定义 $value数组的每一项值 任意定义
    foreach ($arr2 as $key=>$value){
        echo $key.':'.$value.'br/';
    }
?>
------------------------------------------------

<?php
    //请求方式: 接受的url地址栏传递的参数
    //get请求: 定义接受的变量 wd
    //网络请求: http请求 get/post
    //post请求: 一班传递数据from
    //put请求: 修改修改
    //deleta请求: 删除某个请求
    $code=$_GET['wd'];
    if($code){
        echo '查询的内容很多很多----'.$code;

    }


?>
------------------------------------------------

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h2>登录信息提示----传统的web请求</h2>
    <!--
        form属性：
            表单控件：input属性 name 获取用户输入的值
            action='' 点击提交按钮 把当前的form数据提交的位置
            method='get/post' 提交的方式
    -->
    <form action="06form.php" method="POST"> 

        <p>账号:<input type="text" id="" name="username"></p>  
        <p>密码:<input type="text" id="" name="password"></p>  

        <input type="submit" name="" id="" value="登录">
    </form>


</body>
</html>
------------------------------------------------

<?php

    //后端定义 接受表单数据
    // $unname=$_GET['username'];
    // $upwd=$_GET['password'];
    //

    //post
    $uname=$_POST['username'];
    $upwd=$_POST['password'];

    //echo "输入你的账号和密码为: $uname $upwd";
    //本地假设: 账号=admin 密码=123
    if($uname=='admin' && $upwd==123){
        echo '登录成功--进入首页';
    }else{
        echo '账号或密码错误';
    }

?>
------------------------------------------------



















