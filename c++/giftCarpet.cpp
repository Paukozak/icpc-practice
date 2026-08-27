// https://codeforces.com/problemset/problem/1862/A

#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int t, n, m; // n es filas, m columnas, t test cases 
    bool v, i, k, a, diffv, diffi, diffk; //flags

    cin >> t;
    for (int j=0; j< t; j++){
        cin >> n >> m;
        v = false;
        i = false;
        k = false;
        a = false;
        diffv = false;
        diffi = false;
        diffk = false;
        vector<string> matriz(n);    
        for (int o=0; o<n; o++){ //llenado de la matriz
            cin >> matriz[o];
        }
        if (m < 4){
            cout << "NO" << "\n"; 
            continue;
        } else {
        

        for (int p=0; p<m; p++){ //recorro la matriz por columna, no por fila
            for (int o=0; o<n; o++){
                if (matriz[o][p] == 'v'){
                    v = true;
                } 
                if ((matriz[o][p] == 'i' && v && diffv)){
                    i = true;
                } 
                if ((matriz[o][p] == 'k' && i && diffi)){
                    k = true;
                } 
                if ((matriz[o][p] == 'a' && k && diffk)){
                    a = true;
                    break;
                }

            } // cambio de columna
            if (v){
                diffv = true;
            } 
            if(i){
                diffi = true;
            } 
            if(k){
                diffk = true;
            } 
    } //cambio de fila
    if (v && i && k && a){
            cout << "YES" << "\n"; 
        } else {
            cout << "NO" << "\n";
        }    
    }
    }
    

    return 0;
}