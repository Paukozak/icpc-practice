// https://codeforces.com/problemset/problem/445/A

#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, m;

    cin >> n >> m;
    vector<string> matriz(n); // crea un vector de n strings
    for (int i = 0; i < n; i++)
    {
        cin >> matriz[i];
    }

    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            // el color depende de la paridad de (i + j)
            if (matriz[i][j] == '.')
            {
                matriz[i][j] = ((i + j) % 2) ? 'W' : 'B';
            }
        }
        cout << matriz[i] << "\n";
    }

    return 0;
}
