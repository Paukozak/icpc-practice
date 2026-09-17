#include <bits/stdc++.h>

using namespace std;

int main () {

    ios::sync_with_stdio(0);
    cin.tie(0);

    int n, num;
    cin >> n;
    vector<int> clave={0, 5, 1, 6, 2, 7, 3, 8, 4};

    for (int i=0; i<n; i++){
        cin >>num;
        cout << clave[num] << " ";
    }

    return 0;
    }