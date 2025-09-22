import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        // Please write your code here.
        Scanner sc = new Scanner(System.in);
        String a = sc.next();
        String b = "a";
        String text_1 = a.substring(0,1);
        String text_2 = a.substring(2,a.length()-2);
        String text_3 = a.substring(a.length()-1);
        System.out.print(text_1 + b + text_2 + b + text_3);

    }
}