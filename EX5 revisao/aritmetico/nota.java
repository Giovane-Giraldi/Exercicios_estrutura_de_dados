import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner gi = new Scanner(System.in);

        System.out.print("Digite a primeira nota:\n");
        float n1 = gi.nextFloat();
        System.out.println("Nota 1: " +n1);
        System.out.print("Digite a segunda nota:\n");
        float n2 = gi.nextFloat();
        System.out.println("Nota 2: " +n2);
        float media = (n1 + n2) / 2;
        System.out.println("A média é: " + media);
    }
}
