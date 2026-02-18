#include <iostream>
#include <vector>
using namespace std;

int main () {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n;
    cin>>n;

    vector<int> rojo(n);
    for (int i = 0; i < n; i++) {
        cin >> rojo[i];
    }
    vector<int> azul(n);
    for (int i = 0; i < n; i++) {
        cin >> azul[i];
    }

    sort(rojo.begin(),rojo.end());
    
    sort(azul.rbegin(),azul.rend());

    for (int i=0;i<n;i++) {
        rojo[i]+=azul[i];
    }

    sort(rojo.begin(),rojo.end());

    int paint;
    paint= rojo[n-1]-rojo[0];
    
    cout<<paint;

    return 0;


}