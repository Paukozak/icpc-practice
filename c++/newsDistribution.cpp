// https://codeforces.com/problemset/problem/1167/C

//no funciona porque se pasa del tiempo :(

#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
0
vector<int> padre;

void inicializar(int n) {
	padre.resize(n); //el vector padre tiene n elementos
	for (int i = 0; i < n; i++) {
 		padre[i] = i; // al principio, cada uno es padre de sí mismo
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
 	}
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m, x, ac, ant, cont;
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

    for (int i=0; i<n+1; i++) {
        cont=1;

        for (int j=0; j<n+1; j++) {
            if (j!=i) {
                if (encontrar(i)==encontrar(j)) {
                    cont+=1;
                }
            }
        }

        result[i]=cont;
    }


    
    for (int i=1; i<=n; i++) {
        cout << result[i] << " ";
    }


    return 0;
}