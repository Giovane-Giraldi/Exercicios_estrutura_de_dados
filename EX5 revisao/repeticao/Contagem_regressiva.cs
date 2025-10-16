using System;

class Program {
    static void Main() {
        Console.Write("Digite um números para a contagem regressiva:\n");
        int num = int.Parse(Console.ReadLine());
        
        for(int i = num; i >= 1; i--){
          Console.WriteLine(i);    
        }
      Console.WriteLine("FIM!");
    }
  
}
