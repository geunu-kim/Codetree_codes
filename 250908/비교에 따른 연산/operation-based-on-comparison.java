import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        // Please write your code here.
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();
        if (a > b) {
            int c = (a*b);
            System.out.println(c);
        } else {
            int d = (b/a);
            System.out.println(d);
        }
    }
}