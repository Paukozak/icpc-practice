//Beautiful Matrix (263A): https://codeforces.com/problemset/problem/263/A

#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, cant;
    pair<int, int> pos;

    for (int i = 1; i <= 5; i++) {
        for (int j = 1; j <= 5; j++) {
            cin>>n;
            if (n==1) {
                pos = {i, j};
            }
        }
    }

    cant=std::abs(3-pos.first)+std::abs(3-pos.second); 

    cout<<cant;

    
    return 0;
}