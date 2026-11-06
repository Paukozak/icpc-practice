#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

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

    int n, m, k, idioma, tot;

    cin>>n>>m;
    tot=0;

    inicializar(n+m);

   
    for (int i=0; i<n; i++) {
        cin>>k;
        for (int j=0; j<k; j++) {
            cin>>idioma;
            tot+=idioma;
            idioma=idioma-1;
            unir(i, n+idioma);
        }
    }

    if (tot==0) {
        cout<<n;
    } else {
        set<int> grupos;

        for (int i=0; i<n; i++) {
            grupos.insert(encontrar(i));
        }

        cout<<grupos.size()-1;
    }



    return 0;

}