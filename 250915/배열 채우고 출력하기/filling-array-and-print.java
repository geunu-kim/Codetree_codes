import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        // Please write your code here.
        String[] original = new String[10];
        String[] reversed = new String[10];
        Scanner sc = new Scanner(System.in);
        for (int i = 0; i < 10 ; i++){
            original[i] = sc.next();
            reversed[9-i] = original[i];
        }
        for (int i = 0; i < 10; i++){
            System.out.print(reversed[i]);
        }
    }
}