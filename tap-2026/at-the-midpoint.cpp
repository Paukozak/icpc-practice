#include <bits/stdc++.h>

using namespace std;

int main () {

    ios::sync_with_stdio(0);
    cin.tie(0);

    int horas, minutos, segundos;

    cin>>horas>>minutos>>segundos;

    if (horas==2){
        if (minutos==30){
            if (segundos==0){
                cout<<"=";
            } else{
                cout<<"+";
            }
        } else if (minutos<30){
            cout<<"-";
        } else {
            cout << "+";
        }
    } else if (horas<2){
        cout<<"-";
    } else {
        cout<<"+";
    }

    return 0;
}