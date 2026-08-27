// https://codeforces.com/problemset/problem/580/A

#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    
    
    cin>>n;
    vector<int> dias(n, 0);
    vector<int> longitudes(n, 1);
    for (int i=0; i<n; i++){
        cin>>dias[i];
    }

    for (int j = 1; j < n; j++) {
        if (dias[j] >= dias[j - 1]) {
            longitudes[j] = longitudes[j - 1] + 1;
        }
    }
        


    cout << *max_element(longitudes.begin(), longitudes.end());

    return 0;
}