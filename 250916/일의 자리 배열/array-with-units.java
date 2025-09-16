import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        // Please write your code here.
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();
        System.out.print(a + " ");
        System.out.print(b + " ");
        for (int i = 0; i <= 7; i++){
            int c = (a + b) % 10;
            System.out.print(c + " ");
            a = b;
            b = c;
        }
    }
}