//https://codeforces.com/gym/106054/problem/A

#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string s;
    bool hayT, hayA, hayP;

    cin>>s;

    hayT=false;
    hayA=false;
    hayP=false;

    for (int i=0; i<s.size(); i++) {
        if (s[i]=='T') {
            hayT=true;
        } else {
            if (hayT==true) {
                if (s[i]=='A') {
                    hayA=true;
                } else {
                    if (hayA==true) {
                        if (s[i]=='P') {
                            hayP=true;
                        }
                    }
                }
            }
        }
        
    }

    if (hayP==true) {
        cout << "S";
    } else {
        cout << "N";
    }

    return 0;
}