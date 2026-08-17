#include<bits/stdc++.h>

using namespace std;

int main () {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n,aux,m,cont;
    cin>>n;
    cont=0;
    for (int i=0; i<n; i++){
        aux=0;
        for (int j=0; j<3;j++){
            cin>>m;
            if (m==1){
                aux+=1;
            }
        }
        if (aux>=2){
            cont+=1;
        }
    }
    cout<<cont;
        
    return 0;
}