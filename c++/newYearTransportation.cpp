// https://codeforces.com/problemset/problem/500/A

#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, t, j;
    j = 0;
    cin >> n >> t;
    vector<int> portals(n); // la posición portals[i] es la celda, el valor en la posición es i + la celda a la que saltas.
    // es n-2 porque empieza en 0 y porque tenes n-1 portales para n celdas.

    for (int i = 0; i < n; i++)
    {
        cin >> portals[i];
    }

    while ((j + 1) < t)
    {
        j += portals[j];
    }

    if ((j + 1) == t)
    {
        cout << "YES";
    }
    else
    {
        cout << "NO";
    }

    return 0;
}