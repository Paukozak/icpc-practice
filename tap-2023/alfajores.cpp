#include <bits/stdc++.h>

using namespace std;

int main () {
    ios::sync_with_stdio(0);
    cin.tie(0);


    long long n,m, minimo;
    cin>>n>>m;
    unordered_map<long long, long long> cache;
    vector<long long> alfajores(n);
    for (int i=0;i<n;i++){
        cin>>alfajores[i];
    }
    minimo= 10000000000;
    vector<long long> empleados(m);
    vector<long long> empleados_posta;
    for (int i=0;i<m;i++){
        cin>>empleados[i];
        if (empleados[i]<minimo){
            empleados_posta.push_back(empleados[i]);
            minimo=empleados[i];
        }
    }
    long long resto;
    for (int i=0; i<n;i++){
        if (cache.contains(alfajores[i])){
            cout<< cache[alfajores[i]]<< " ";
            continue;
        }
        resto=alfajores[i];
        int pos=0;
        while (pos<empleados_posta.size()){
            auto it = lower_bound(empleados_posta.begin() + pos, empleados_posta.end(), resto, greater<long long>());
            if (it == empleados_posta.end()) {
                // No hay más oficinas que puedan repartir
                break;
            }
            int nueva_pos = distance(empleados_posta.begin(), it);
            resto %= empleados_posta[nueva_pos];
            pos = nueva_pos + 1;
            if (resto==0) break;
        }
        cache[alfajores[i]]=resto;
        cout<<resto<<" ";
    }


    return 0;
}