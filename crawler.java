// 匹配http://www.runoob.com/java/java-regular-expressions.html中所有表格中的内容并打印出来

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.net.URL;
import java.net.URLConnection;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class crawler{
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
        Pattern pattern = Pattern.compile(patternStr);  // complie first
        Matcher matcher = pattern.matcher(targetStr);  // then match
        String rm_title = "</?\\S*?>";
        Pattern rm_pattern = Pattern.compile(rm_title);
        while (matcher.find()){  // matcher.find()是逐步进行，因此要通过循环来显示出所有结果
            String content = matcher.group();
            Matcher matcher2 = rm_pattern.matcher(content);
            result += matcher2.replaceAll("") + "\n";
        }
        return result;
    }

    public static void main(String args[]){
        String url = "http://www.runoob.com/java/java-regular-expressions.html";
        String result = sendHTML(url);
        String patternStr = "<td>.*?<p>(.*?)</p>.*?</td>";
        String content = ReStr(result, patternStr);
        System.out.println(content);
    }
}