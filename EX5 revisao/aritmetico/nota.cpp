#include <iostream>
using namespace std;

int main() {
    float n1, n2, media;
    cout << "Digite a primeira nota: \n";
    cin >> n1;
    cout << "Nota 1: " << n1 << endl;
    cout << "Digite a segunda nota: \n";
    cin >> n2;
    cout << "Nota 2: " << n2 << endl;

    media = (n1 + n2) / 2;

    cout << "A média é: " << media << endl;
    return 0;
}