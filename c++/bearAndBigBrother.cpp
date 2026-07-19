//Bear and Big Brother (791A): https://codeforces.com/problemset/problem/791/A

#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int a, b, y;

    cin>>a>>b;

    y=0;

    while (a<=b) {
        a=a*3;
        b=b*2;
        y+=1;
    }

    cout<<y;

    return 0;
}