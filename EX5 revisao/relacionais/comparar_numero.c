#include <stdio.h>

int main() {
    float a, b;
    printf("Digite dois números: ");
    scanf("%f %f", &a, &b);

    if (a > b)
        printf("%.1f é maior que %.1f\n", a, b);
    else if (a < b)
        printf("%.1f é menor que %1.f\n", a, b);
    else
        printf("Os números são iguais\n");

    return 0;
}