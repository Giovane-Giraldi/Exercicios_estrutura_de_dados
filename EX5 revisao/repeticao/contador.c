#include <stdio.h>

int main() {
  int n,limite;
  n = 0;
  printf("Digite um número a ser contado");
  scanf("%d", &limite);
  printf("%d", n);
  while(n <= limite){
    printf("%d\n", n);
    n++;
    
  }
  return 0;
}