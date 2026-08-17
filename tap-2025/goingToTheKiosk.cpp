#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int a, b, c;

    cin>>a>>b>>c;

    if (((b-a) % c)==0) {
        cout<<"S";
    } else {
        cout<<"N";
    }


    return 0;
}