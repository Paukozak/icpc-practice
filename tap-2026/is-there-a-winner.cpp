#include <bits/stdc++.h>

using namespace std;

int main () {

    ios::sync_with_stdio(0);
    cin.tie(0);

    int jug,rondas;

    cin>>jug>>rondas;

    if (rondas==1){
        cout<<"S";
    } else if (jug==2 and (rondas%2)==1){
        cout<<"S";
    }else{
        cout <<"N";
    }

    return 0;
    }