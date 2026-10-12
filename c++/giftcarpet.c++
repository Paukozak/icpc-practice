#include <bits/stdc++.h>

using namespace std;

int main () {

    ios::sync_with_stdio(0);
    cin.tie(0);

    int t, n, m;
    vector<string> line(n); 
    bool v,i,k,a;   
    cin >>t;
    for (i=0; i<t; i++){
        cin >> n >> m;
        cin >> line[0];
        v=false;
        i=false;
        k=false;
        a=false;

        if (m<3){
            cout << "NO";
        } else {
            for (j=0; j<m; j++)<{
                for (k=0;k<n;k++){
                    if ((line[k][n]=='v') && not v ){
                        v=true;
                        continue;
                    }
                    if ((line[k][n]=='i') && not i && v){
                        i=true;
                        continue;
                    }
                    if ((line[k][n]=='k') && not k && i ){
                        k=true;
                        continue;
                    }
                    if ((line[k][n]=='a') && not a && k ){
                        a=true;
                        cout<<"YES";
                        break;
                    } 
                }
            }
        }
    }    


    return 0;
}