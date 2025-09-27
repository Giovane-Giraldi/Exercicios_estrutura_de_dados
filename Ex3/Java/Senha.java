import java.util.*;

public class Main {
    public static void main(String[] args) {
      Scanner input = new Scanner(System.in);
      
      
      System.out.println("Digite a senha!");
      String s = input.nextLine();
      
     
      if(s.equals("User123")){
      System.out.println("Bem-vindo, Usuário!");
      }
      
      else if(s.equals("Admin123")){
      System.out.println("Bem-vindo, Administrador!");
      }
      else{
         System.out.println( "Código incorreto");
    }
  }
}