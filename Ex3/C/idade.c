#include <stdio.h>
int main()
{
  int n;
    printf("Digite sua Idade\n");
  scanf("%d", &n);

  if (n >= 18){
  printf("Você é maior de idade!");
  }
  else {
  printf("Você é menor de idade!");
  }
}