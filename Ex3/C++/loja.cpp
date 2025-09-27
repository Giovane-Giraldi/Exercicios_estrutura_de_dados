#include <iostream>
using namespace std;

int main() {
    int n;
    
    cout << "Digite o valor da compra:\n";
    cin >> n; 
    
    if (n >= 100) {
        cout << "Frete grátis!" << endl;  
    } else {
        n += 15; 
        cout << "O valor total é: " << n << endl;
    }
    
    return 0;
}