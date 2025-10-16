import java.util.Scanner;

public class contador {
    public static void main(String[] args) {
        Scanner gi = new Scanner(System.in);

        System.out.print("Digite o número limite: ");
        int limite = gi.nextInt();

        int n = 0;
        while (n <= limite) {
            System.out.println(n);
            n++;
        }
    }
}
