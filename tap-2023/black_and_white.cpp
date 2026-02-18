#include <iostream>
#include <string>

using namespace std;

int main () {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n;
    cin>>n;
    int cont=0;
    string casillas;
    for (int i=0; i<n; i++ ){
        cin>>casillas;
        
        for (int j=0; j<(n-1);j++){
            if ((casillas[j]=='N') and (casillas[j+1]=='N')){
                cont++;
                j++;
            }
        }
    }
    cout<<cont;
    return 0;
}