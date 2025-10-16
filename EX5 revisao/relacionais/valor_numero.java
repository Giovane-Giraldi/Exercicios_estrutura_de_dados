import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner gi = new Scanner(System.in);

        System.out.print("Digite um número: ");
        int num = gi.nextInt();

        if (num > 0)
            System.out.println("O número " + num +" é positivo.");
        else if (num < 0)
            System.out.println("O número " + num +" é negativo.");
        else
            System.out.println("O número é zero.");
    }
}