#include <bits/stdc++.h>

using namespace std;

int main () {

    ios::sync_with_stdio(0);
    cin.tie(0);

    int cant, velocidad, tamaño, pos;
    cin>>cant>>velocidad;



    char prio;
    string lista;
    vector<double> tamaño_prio, tamaño_unprio;

    for (int i=0; i<cant; i++) {
        cin>>prio>>tamaño;
        if (prio==*"P"){
            tamaño_prio.push_back(tamaño);
        } else {
            tamaño_unprio.push_back(tamaño);
        }
    }

    double velocidad_prio, velocidad_unprio, tiempo, tiempo_min,tiempo_total;
    
    tiempo_total=0;
    for (int i=0; i<cant; i++){
        tiempo_min=513;
        if (tamaño_prio.empty()){
            velocidad_unprio=velocidad;
        } else if (tamaño_unprio.empty()){
            velocidad_prio=velocidad;
        } else{
            velocidad_prio=velocidad*0.75;
            velocidad_unprio=velocidad*0.25;
        }

        for (size_t j=0; j<tamaño_prio.size();j++){
            tiempo=tamaño_prio[j]/(velocidad_prio/tamaño_prio.size());
            if (tiempo<tiempo_min){
                tiempo_min=tiempo;
                lista="P";
                pos=j;
            }
            //cout<< "calculo el tiempo menor de las priorizadas"<<"\n";
        }
        for (size_t j=0; j<tamaño_unprio.size();j++){
            tiempo=tamaño_unprio[j]/(velocidad_unprio/tamaño_unprio.size());
            if (tiempo<tiempo_min){
                tiempo_min=tiempo;
                lista="N";
                pos=j;
            }
            //cout <<tamaño_unprio[j];
            //cout << "calculo el tiempo menor de los no priorizadas"<<"\n";
        }

        for (size_t j=0; j<tamaño_prio.size();j++){
            tamaño_prio[j]=tamaño_prio[j]- (tiempo_min*(velocidad_prio/tamaño_prio.size()));
            //cout <<"recalculo la priorizada"<<"\n";
        }

        
        for (size_t j=0; j<tamaño_unprio.size();j++){
            tamaño_unprio[j]=tamaño_unprio[j]- (tiempo_min*(velocidad_unprio/tamaño_unprio.size()));
            //cout <<"recalculo una no priorizada"<<"\n";
        }

        if (lista=="N"){
            tamaño_unprio.erase(tamaño_unprio.begin()+pos);
            //cout<<"borro una no priorizada"<<"\n";
        } else {
            tamaño_prio.erase(tamaño_prio.begin()+pos);
            //cout <<"borro una priorizada"<<"\n";
        }

        

        tiempo_total+=tiempo_min;
        //cout << "sumo tiempo minimo"<<"\n";
        //cout << tiempo_total<< "\n";

    }

    cout<<tiempo_total;

    return 0;
}