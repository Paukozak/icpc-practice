#include <bits/stdc++.h>

using namespace std;

int main () {

    ios::sync_with_stdio(0);
    cin.tie(0);

    string palabra,npalabra;
    vector<char> vocales={'A','E','I','O','U'};
    bool esVocal;
    set<string> palabras; 

    cin>>palabra;

    int n=palabra.length();
    for (int i=0; i<n;i++){
        esVocal=find(vocales.begin(),vocales.end(),palabra[i])!=vocales.end();
        if(esVocal && palabra[i+1]=='G' && palabra[i+2]=='A' && palabra[i+3]=='S' && palabra[i+4]==palabra[i]){
            npalabra=palabra.substr(0,i+1)+palabra.substr(i+5);
            palabras.insert(npalabra);
        }
    }

    if (palabras.empty()){
        cout<<'-';
    } else if (palabras.size()==1){
        cout<<*palabras.begin();
    } else {
        cout<<'+';
    }



    return 0;
    }