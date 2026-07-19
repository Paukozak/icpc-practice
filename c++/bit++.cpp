//Bit++ (282A): https://codeforces.com/problemset/problem/282/A

#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, result;
    string s;

    cin>>n;

    result=0;

    for (int i=0; i<n; i++) {

        cin>>s;

        if (s.find("+") != string::npos) {
            result+=1;
        } else {
            result-=1;
        }

    }

    cout<<result;

    return 0;
}