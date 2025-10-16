using System;

class Program {
    static void Main() {
        Console.WriteLine("Digite a primeira nota: ");
        float n1 = float.Parse(Console.ReadLine());
        Console.WriteLine("Nota 1:"+n1);
        Console.WriteLine("Digite a segunda nota: ");
        float n2 = float.Parse(Console.ReadLine());
        Console.WriteLine("Nota 2:"+n2);
        float media = (n1 + n2) / 2;
        Console.WriteLine("A média é: " + media);
    }
}
