//Nearly Lucky Number (110A): https://codeforces.com/problemset/problem/110/A
 
#include <bits/stdc++.h>
using namespace std;
 
typedef long long ll;
 
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
 
    string s;
    int cant;
    map<char, int> cont;
 
    cin>>s;
 
    for (char c : s) {
        cont[c]++;
    }
 
    cant=cont['4']+cont['7'];
 
    if ((cant==4) || (cant==7)) {
        cout<<"YES";
    } else {
        cout<<"NO";
    }
 
    return 0;
}