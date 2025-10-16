using System;

class Program {
    static void Main() {
        Console.Write("Digite dois números: ");
        int a = int.Parse(Console.ReadLine());
        int b = int.Parse(Console.ReadLine());

        if (a > b)
            Console.WriteLine($"{a} é maior que {b}");
        else if (a < b)
            Console.WriteLine($"{a} é menor que {b}");
        else
            Console.WriteLine("Os números são iguais");
    }
}
