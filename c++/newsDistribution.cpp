// https://codeforces.com/problemset/problem/1167/C

#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

vector<int> padre;
vector<int> tamanio;

void inicializar(int n) {
	padre.resize(n); //el vector padre tiene n elementos
    tamanio.resize(n); 
	for (int i = 0; i < n; i++) {
 		padre[i] = i; // al principio, cada uno es padre de sí mismo
        tamanio[i] = 1;
 	}
}

int encontrar(int x) {
	if (padre[x] == x) return x;
 	return padre[x] = encontrar(padre[x]); // compresión de camino
}

void unir(int a, int b) {
	a = encontrar(a);
	b = encontrar(b);
	if (a != b) {
	padre[a] = b; // el grupo de a pasa a depender del grupo de b
    tamanio[b] += tamanio[a];
 	}
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m, x, ac, ant;
    string grupo;

    cin>>n>>m;

    inicializar(n+1);

    vector<int> result(n);
     

    for (int i=0; i<m; i++) {

        cin>>x;

        ant=0;

        for (int j=0; j<x; j++) {
            cin>>ac;

            if (ant!=0) {
                unir(ac, ant);
            } 

            ant=ac;
        }

    }

    
    for (int i = 1; i <= n; i++) {
        cout << tamanio[encontrar(i)] << " ";
    }


    return 0;
}