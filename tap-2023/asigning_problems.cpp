#include <iostream>
#include <vector>

using namespace std;

int main () {
    ios::sync_with_stdio(0);
    cin.tie(0);

    long long k;
    cin>>k;
    vector<long long> problemas_nivel(k);
    for (int i=0;i<k;i++) {
        cin>>problemas_nivel[i];
    }
    vector <long long> problemas(k);
    vector <long long> pref_sum(k);
    for (int i=0;i<k;i++){
        cin>>problemas[i];
        if(i!=0){
            pref_sum[i]=pref_sum[i-1]+problemas[i];    
        } else {
            pref_sum[i]=problemas[i];
        }
    }
    long long cont,total;
    total=0;
    cont=0;
    for (int i=0;i<k;i++){
        
        if (problemas[i]>problemas_nivel[i]){
            problemas[i]-=problemas_nivel[i];
            cont+=1;
        } else{
            for (int j=1;j<(i+1);j++){
                if ((i-j)>=0 and problemas[i-j]>problemas_nivel[i]){
                    problemas[i-j]-=problemas_nivel[i];
                    cont+=1;
                } else if ((i-j)<0){
                    break;
                }
            }
        }
        if (cont==k){
            total+=1;
            cont=0;}
    }

    cout<<total;



    return 0;
}