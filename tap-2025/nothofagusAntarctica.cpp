#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, mayX, mayY, menX, menY, per;

    pair<int, int> punto;
    vector<pair<int, int>> v;

    mayX=0;
    mayY=0;
    menX=1000000000;
    menY=1000000000;

    cin>>n;

    for (int i=0; i<n; i++) {
        cin>>punto.first;
        cin>>punto.second;

        v.push_back(punto);

        if (punto.first>mayX) {
            mayX=punto.first;
        }
        if (punto.second>mayY) {
            mayY=punto.second;
        }
        if (punto.first<menX) {
            menX=punto.first;
        } 
        if (punto.second<menY) {
            menY=punto.second;
        }

    }

    per=((mayX-menX+2)*2+(mayY-menY+2)*2);

    cout<<per;

    return 0;
}