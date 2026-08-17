//Matrix Rotation (1772B): https://codeforces.com/problemset/problem/1772/B

#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, aux1, aux2;
    vector<vector<int>> matriz(2, vector<int>(2, 0));

    cin>>n;


    for (int x=0; x<n; x++) {

        for (int i=0; i<2; i++) {
            for (int j=0; j<2; j++) {
                cin>>matriz[i][j];
            }
        }
 
        while ((matriz[0][0]>matriz[0][1]) || (matriz[0][0]>matriz[1][1]) || (matriz[0][0]>matriz[1][0])) {
            aux1=matriz[0][0];
            matriz[0][0]=matriz[1][0];
            aux2=matriz[0][1];
            matriz[0][1]=aux1;
            aux1=matriz[1][1];
            matriz[1][1]=aux2;
            matriz[1][0]=aux1;
        }

        if (matriz[0][0] < matriz[0][1]) {
            if (matriz[0][1] < matriz[1][1]) {
                if (matriz[1][0] < matriz[1][1]) {
                    if (matriz[0][0] < matriz[1][0]) {
                        cout<<"YES"<< "\n";
                    } else {
                        cout<<"NO"<< "\n";
                    }
                } else {
                    cout<<"NO"<< "\n";
                }
            } else {
                cout<<"NO"<< "\n";
            }
        } else {
            cout<<"NO"<< "\n";
        }


    }


    return 0;
}