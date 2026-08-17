//https://codeforces.com/gym/106054/problem/I

#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m, x, c1, og;
    pair<int, int> money;

    cin>>n>>m;

    vector<int> players(n+1, 0);
    vector<int> choices(n+1);

    for (int i=0; i<m; i++) {
        cin>>money.first;
        cin>>money.second;
        c1=0;

        for (int j=0; j<n; j++) {
            cin>>x;
            if (x==1) {
                c1+=1;
                choices[j]=1;
            } else {
                choices[j]=2;
            }
        }
        
        og=money.first;

        money.first=(money.first/(c1+1));
        
        if (money.first>=money.second) {
            choices[n]=1;
        } else {
            choices[n]=2;
            if (c1>0) {
                money.first=(og/c1);
            }
        }

        for (int j=0; j<(n+1); j++) {
            if (choices[j]==1) {
               players[j]+=money.first; 
            } else {
                players[j]+=money.second;
            }
        }
        
    }

    for (int x : players) {
        cout << x << " ";
    }


    return 0;
}