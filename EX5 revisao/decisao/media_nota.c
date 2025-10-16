#include <stdio.h>
int main()
{
  float n1, n2, media;
  
  printf("Digite a primeira nota\n");
  scanf("%f", &n1);
  printf("nota 1: %.1f\n", n1);
  printf("Digite a segunda nota\n");
  scanf("%f", &n2);
  printf("nota 2: %.1f\n", n2);
  
  media = (n1 +n2)/2;
  
  printf("A media é: %.2f\n", media);

  
  if(media<5)
    printf("REPROVADO");
  else if(media<6)
    printf("RECUPERAÇÃO");
  else
    printf("APROVADO");
    return 0;
}