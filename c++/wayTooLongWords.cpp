//Way Too Long Words (71A): https://codeforces.com/problemset/problem/71/A

#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int n, num;
    string ent, sal, valor;
    cin>>n;

    for (int i = 0; i < n; i++) {
        
        cin>>ent;

        if (ent.size() > 10) {
            num=(ent.size())-2;
            valor=to_string(num);
            sal=ent[0]+valor+ent[ent.size()-1];
        } else {
            sal=ent;
        }

        cout<<sal<<"\n";

    }




    return 0;
}