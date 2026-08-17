#include <iostream>
#include <vector>

using namespace std;

int main () {
    ios::sync_with_stdio(0);
    cin.tie(0);

    long long k;
    cin>>k;
    vector<long long> problemas_nivel(k);
    vector <long long> pref_sum_niveles(k);
    for (int i=0;i<k;i++) {
        cin>>problemas_nivel[i];
        if(i!=0){
            pref_sum_niveles[i]=pref_sum_niveles[i-1]+problemas_nivel[i];    
        } else {
            pref_sum_niveles[i]=problemas_nivel[i];
        }
    }
    vector <long long> problemas(k);
    vector <long long> pref_sum_problemas(k);
    for (int i=0;i<k;i++){
        cin>>problemas[i];
        if(i!=0){
            pref_sum_problemas[i]=pref_sum_problemas[i-1]+problemas[i];    
        } else {
            pref_sum_problemas[i]=problemas[i];
        }
    }
    long long cont;

    cont=10000000000;
    for (int i=0; i<k; i++){
        if ((pref_sum_problemas[i]/pref_sum_niveles[i])<cont){
            cont=pref_sum_problemas[i]/pref_sum_niveles[i];
        }
    }

    cout<<cont;

    return 0;
}