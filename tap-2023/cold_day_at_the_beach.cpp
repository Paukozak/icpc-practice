#include <iostream>
#include <vector>
using namespace std;

int main () {
    ios::sync_with_stdio(0);
    cin.tie(0);
    int n,w,l,tx,ty;

    cin>>n>>w>>l>>tx>>ty;
    vector<int> distA(n);
    vector<int> azul(n*2);
    for (int i=0; i<(n*2);i++){
        cin>>azul[i];
        if ((i%2)==1){
            distA[(i-1)/2]=(tx-azul[i-1])*(tx-azul[i-1])+(ty-azul[i])*(ty-azul[i]);
        }
    }

    vector<int> rojo(n*2);
    vector<int> distR(n);
    for (int i=0; i<(n*2);i++){
        cin>>rojo[i];
        if ((i%2)==1){
            distR[(i-1)/2]=(tx-rojo[i-1])*(tx-rojo[i-1])+(ty-rojo[i])*(ty-rojo[i]);
        }
    }

    sort(distR.begin(),distR.end());
    sort(distA.begin(),distA.end());
    int puntos=1;

    if (distA[0]<distR[0]){
        for (int i=1;i<n;i++){
            if (distA[i]<distR[0]){
                puntos+=1;
            } else {
                break;
            }
        }
        cout<<"A "<<puntos;
    } else {
        for (int i=1;i<n;i++){
            if (distR[i]<distA[0]){
                puntos+=1;
            } else {                
                break;
            }
        }
        cout<<"R "<<puntos;
    }
    
    return 0;
}