// 爬取http://www.wikicfp.com/cfp/相应表格的内容并且写入数据库

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.net.URL;
import java.net.URLConnection;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
import java.sql.*;

public class crawler3{

    // final用来设定为常量
    static final String JDBC_DRIVER = "com.mysql.jdbc.Driver";  // 数据库驱动
    static final String DB_URL = "jdbc:mysql://localhost:3306/java?useUnicode=true&characterEncoding=utf8&useSSL=false";

    // 数据库的用户名与密码，需要根据自己的设置
    static final String USER = "USER";
    static final String PASS = "PASS";


    static String sendHTML(String url){
        String result = "";
        BufferedReader in = null;  // 定义一个缓冲字符输入流
        try{
            URL readUrl = new URL(url);  // read URL
            URLConnection conn = readUrl.openConnection();
            conn.connect();  // send GET request
            in = new BufferedReader(new InputStreamReader(conn.getInputStream()));
            String line;
            while ((line = in.readLine()) != null){
                result += line + "\n";  // 一行行的写进
            }
        } catch (Exception e){
            System.out.println("GET请求发送异常！" + e);
            e.printStackTrace();
        }
        finally{
            try{
                if (in != null){
                    in.close();
                }
            } catch (Exception e2){
                e2.printStackTrace();
            }
        }
        return result;
    }

    static String ReStr(String targetStr, String patternStr){
        String result = "";
        Pattern pattern = Pattern.compile(patternStr);  // 先编译表达式
        Matcher matcher = pattern.matcher(targetStr);  // 再匹配
        // 用来匹配掉html标签
        String rm_title = "</?\\S.*?>";
        Pattern rm_pattern = Pattern.compile(rm_title);
        while (matcher.find()){  // matcher.find()是逐步进行，因此要通过循环来显示出所有结果
            String content = matcher.group(1);  // 由于正则中加了括号，因此为组的元素
            Matcher matcher2 = rm_pattern.matcher(content);  // html标签什么的都消失吧
            result += matcher2.replaceAll("") + "\n";
        }
        return result;
    }

    static void IntoDB(String event, String detail, String time){
        Connection conn = null;
        Statement stmt = null;


        try {
            System.out.println("Begin.");
            Class.forName("com.mysql.jdbc.Driver");
            conn = DriverManager.getConnection(DB_URL, USER, PASS);
            // 后面的values括号里面要加单引号，不然结果会出错
            String SQL = String.format("INSERT INTO meetings (event, detail, time) VALUES ('%s', '%s', '%s')", event, detail, time);  
            System.out.println(SQL);
            stmt = conn.createStatement();
            // 这里INSERT，UPDATE等操作用的是executeUpdate，而SELECT用的是execute()
            int rs = stmt.executeUpdate(SQL);  
            System.out.println("End.");

        }
        catch (Exception e) {
            e.printStackTrace();
        } finally {
            if (stmt != null)
                try {
                    stmt.close();
                } catch (Exception e) {
                    e.printStackTrace();
                }
            if (conn != null)
                try {
                    conn.close();
                } catch (Exception e) {
                    e.printStackTrace();
                }
        }
    }

    public static void main(String args[]){
        String url = "http://www.wikicfp.com/cfp/";
        String result = sendHTML(url);
        // 匹配
        String patternStr1 = "<td rowspan=\"2\".*?>(.*?)</td>";
        String event = ReStr(result, patternStr1);
        String evt[] = event.split("\n");  // 把字符串拆分成字符数组，和Python几乎一样
        
        String patternStr2 = "<td align=\"left\" col.*?>(.*?)</td>";
        String detail = ReStr(result, patternStr2);
        String dtl[] = detail.split("\n");
        
        String patternStr3 = "<td align=\"left\">([A-Z].*?)</td>";
        String time = ReStr(result, patternStr3);
        String tm[] = time.split("\n");
        // 输出并且存入数据库
        int i = 0;
        while (i < evt.length){
            System.out.println("Event:" + evt[i]);
            System.out.println("Detail:" + dtl[i]);
            System.out.println("Time:");
            System.out.println(tm[i * 3]);
            System.out.println(tm[i * 3 + 1]);
            System.out.println(tm[i * 3 + 2] + "\n\n");
            String times = tm[i * 3] + tm[i * 3 + 1] + tm[i * 3 + 2];
            IntoDB(evt[i], dtl[i], times);
            i += 1;
        }
    }
}
