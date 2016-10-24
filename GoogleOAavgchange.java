/**
 * Created by zyj on 2016/10/6.
 */
import java.util.*;

public class GoogleOAavgchange{
    public static int avgchange(int num) {
        Integer input=new Integer(num), result=0;
        String in=input.toString();
        char ch1,ch2,newch;
        int n=in.length();
        for (int i=0;i<n-1;i++) {
            StringBuilder inputs=new StringBuilder(input.toString());
            ch1=inputs.charAt(i);
            ch2=inputs.charAt(i+1);
            newch=(char)(((int)ch1+1+(int)ch2)/2);
            inputs.setCharAt(i,newch);
            inputs.delete(i,i+1);
            if (result<Integer.parseInt(inputs.toString())) {
                result=Integer.parseInt(inputs.toString());
            }
        }
        return result;
    }
    public static void main(String[] args) {
        int num=623315;
        System.out.println(avgchange(num));
    }
}