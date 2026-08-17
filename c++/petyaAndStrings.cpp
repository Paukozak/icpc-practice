//Petya and Strings (112A): https://codeforces.com/problemset/problem/112/A

#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string s1, s2;
    char c1, c2;
    int sal, i;
    bool fin;

    sal=0;

    cin>>s1>>s2;

    i=0;
    fin=false;

    while ((i<(s1.size())) && fin==false) {

        c1=tolower(s1[i]);
        c2=tolower(s2[i]);

        if (c1!=c2) {
            fin=true;
            if (c1>c2) {
                sal=1;
            } else {
                sal=-1;
            }
        }

        i+=1;

    }

    cout<<sal;

    return 0;
}