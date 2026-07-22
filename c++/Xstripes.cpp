//Stipes (1742C): https://codeforces.com/problemset/problem/1742/C

//No esta resuelto :)

#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, contb, contr;

    string x;

    cin>>n;

    vector<string> v(n);


    for (int i=0; i<n; i++) {

        contb=0;
        contr=0;

        for (int j=0; j<8; j++) {

            cin>>x;

            cout<<"recibi esto: "<<x<< "\n";

            for (char c : x) {
                if (c=='B') {
                    contb+=1;
                } else if (c=='R') {
                    contr+=1;
                }
            }

            
            cout<<j<<"\n";
        }
        
        if (contb>contr) {
            v[i]="B";
            cout<<"gano b"<< "\n";
        } else {
            v[i]="R";
            cout<<"gano r"<< "\n";
        }

        cout<<contb<<" "<<contr;

    }
 
    for (string y : v) {
        cout << y << "\n";
    }

    return 0;
}