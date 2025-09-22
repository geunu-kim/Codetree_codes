import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        // Please write your code here.
        Scanner sc = new Scanner(System.in);
        String a = sc.next();
        String b = sc.next();
        int c = a.length();
        int d = b.length();
        if (c > d) {
            System.out.print(a + " ");
            System.out.print(c);
        } else if (c == d) {
            System.out.println("same");
        } else {
            System.out.print(b + " ");
            System.out.print(d);
        }
}
}