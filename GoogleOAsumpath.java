/**
 * Created by zyj on 2016/10/6.
 */
import java.util.*;

public class GoogleOAsumpath {
    public static int sumpath(String s) {
        List<Integer> level=new ArrayList<Integer>();
        String ext;
        String[] lines=s.split("\n");
        int result=0,count,pos;
        level.add(0);
        for (int i=0;i<lines.length;i++) {
            pos=lines[i].lastIndexOf(' ');
            if (pos==-1) {
                count=1;
            }
            else {
                count=pos+2;
            }
            pos=lines[i].indexOf('.');
            if (pos==-1) {
                if (level.size()<count+1) {
                    level.add(level.get(count-1)+lines[i].length()-count+2);
                }
                else {
                    level.set(count,level.get(count-1)+lines[i].length()-count+2);
                }
            }
            else {
                ext=lines[i].substring(pos+1);
                if ((ext.equals("jpeg"))||(ext.equals("png"))||(ext.equals("gif"))) {
                    result+=(level.get(count-1)+lines[i].length()-count+2)%1000000007;
                }
            }
        }
        return result;
    }
    public static void main(String[] args) {
        String s="dir1\n dir11\n dir12\n  picture.jpeg\n  dir121\n   file1.txt\ndir2\n file2.gif";
        System.out.println(sumpath(s));
        s = "file.png\nfile.test\nfile.jpeg";
        System.out.println(sumpath(s));
        s= "DER1\n dir11\n dir12\n  picture.jPeg\n  dir121\n   file1.txt\ndir2\n file2.gIf";
        System.out.println(sumpath(s));
    }
}
