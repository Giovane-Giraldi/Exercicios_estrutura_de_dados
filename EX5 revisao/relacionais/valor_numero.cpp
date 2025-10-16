#include <iostream>
using namespace std;

int main() {
    float n;
    cout << "Digite um número: \n";
    cin >> n;
    
    if(n < 0)
    cout << "O numero "<< n<<" é negativo\n";
    else if(n > 0)
    cout << "O numero "<< n <<" é positivo\n";
    else
    cout << " O numero é zero\n";
}