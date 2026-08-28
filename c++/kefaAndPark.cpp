#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

int n, m, h, o, restaurantes;
vector<vector<int>> ady;
vector<bool> visitado;
vector<int> nodos;

void dfs(int u, int padre, int gatosConsecutivos)
{
    visitado[u] = true; // marca el nodo actual como visitado.
    // acá se procesa el nodo u (contarlo, sumarlo, imprimirlo, etc.)
    if (nodos[u] == 1)
    {
        gatosConsecutivos++;
    }
    else
    {
        gatosConsecutivos = 0;
    }
    if (gatosConsecutivos > m) // si se pasa de los gatos
    {
        return;
    }

    bool esHoja = true;

    for (int v : ady[u])
    {
        if (v == padre)
            continue;

        esHoja = false;
        dfs(v, u, gatosConsecutivos);
    }

    if (esHoja)
        restaurantes++;
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> n >> m;
    restaurantes = 0;

    nodos.resize(n + 1);
    ady.resize(n + 1); // cada indice representa un nodo, en cada posición está la lista de nodos conectados

    for (int i = 1; i <= n; i++)
    {
        cin >> nodos[i];
    }

    for (int i = 0; i < n - 1; i++)
    {
        cin >> h >> o;
        ady[h].push_back(o);
        ady[o].push_back(h);
    }

    visitado.assign(n + 1, false);
    dfs(1, 0, 0); // recorre todo lo alcanzable desde el nodo 1
    cout << restaurantes;

    return 0;
}
