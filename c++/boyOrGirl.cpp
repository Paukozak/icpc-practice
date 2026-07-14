//Boy or Girl (236A): https://codeforces.com/problemset/problem/236/A 

#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string username;

    cin>>username;

    std::set<char> usrSet(username.begin(), username.end()); 

    if (((usrSet.size()) % 2) == 0) {
        cout<<"CHAT WITH HER!";
    } else {
        cout<<"IGNORE HIM!";
    }


    return 0;
}