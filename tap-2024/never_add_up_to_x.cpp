#include <bits/stdc++.h>
using namespace std;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    long long N, X;
    cin >> N >> X;

    unordered_map<long long,long long> cnt;
    cnt.reserve(N*2);
    for(int i=0;i<N;i++){
        long long b; cin >> b;
        cnt[b]++;
    }

    // Valor auto-emparejado (si X es par, X/2 + X/2 = X, así que no puede
    // haber dos copias de X/2 adyacentes entre sí).
    long long m = -1, cm = 0;
    if(X % 2 == 0){
        m = X/2;
        auto it = cnt.find(m);
        if(it != cnt.end()) cm = it->second;
    }

    // El resto de los valores se agrupan en pares (v, X-v). Si el compañero
    // X-v no aparece en el arreglo, v es "libre" (puede ir adyacente a
    // cualquier cosa sin problema).
    vector<long long> leftVals, rightVals, freeVals;
    unordered_set<long long> visited;

    for(auto &pr : cnt){
        long long v = pr.first;
        if(v == m) continue;
        if(visited.count(v)) continue;
        long long p = X - v;
        auto it = (p >= 1 && p <= X) ? cnt.find(p) : cnt.end();
        if(p != v && it != cnt.end() && it->second > 0){
            leftVals.push_back(v);
            rightVals.push_back(p);
            visited.insert(v);
            visited.insert(p);
        } else {
            freeVals.push_back(v);
            visited.insert(v);
        }
    }

    long long numPairs = (long long)leftVals.size();
    long long numFrees = (long long)freeVals.size();

    vector<long long> core;
    core.reserve(N - cm);
    long long mandatoryGap = -1; // gap que obligatoriamente debe llevar un "m"

    auto appendBlock = [&](long long val){
        long long c = cnt[val];
        for(long long i=0;i<c;i++) core.push_back(val);
    };

    if(numPairs == 0){
        // Sin pares conflictivos: cualquier orden de los valores libres sirve.
        for(long long v : freeVals) appendBlock(v);
    } else if(numPairs == 1){
        // Un solo par conflictivo: hay que separar el bloque izquierdo del
        // derecho con algo en el medio (valores libres, o si no hay, un "m").
        appendBlock(leftVals[0]);
        long long afterLeftSize = (long long)core.size();
        for(long long v : freeVals) appendBlock(v);
        appendBlock(rightVals[0]);
        if(numFrees == 0) mandatoryGap = afterLeftSize;
    } else {
        // Dos o más pares: se arman todos los bloques "izquierdos" seguidos
        // de todos los "derechos" en el MISMO orden. El único borde riesgoso
        // queda entre el último izquierdo y el primer derecho, que
        // pertenecen a pares DISTINTOS, así que nunca sumo X entre ellos.
        for(long long v : leftVals) appendBlock(v);
        for(long long v : rightVals) appendBlock(v);
        for(long long v : freeVals) appendBlock(v);
    }

    long long L = (long long)core.size();
    long long G = L + 1; // cantidad de huecos disponibles para insertar "m"

    bool possible = true;
    if(mandatoryGap != -1 && cm == 0) possible = false;
    if(cm > G) possible = false;

    if(!possible){
        cout << "*\n";
        return 0;
    }

    vector<char> useGap(G, 0);
    long long remaining = cm;
    if(mandatoryGap != -1){
        useGap[mandatoryGap] = 1;
        remaining--;
    }
    for(long long g = 0; g < G && remaining > 0; g++){
        if(useGap[g]) continue;
        useGap[g] = 1;
        remaining--;
    }

    vector<long long> result;
    result.reserve(N);
    for(long long i = 0; i <= L; i++){
        if(useGap[i]) result.push_back(m);
        if(i < L) result.push_back(core[i]);
    }

    for(int i = 0; i < (int)result.size(); i++){
        cout << result[i] << (i+1 < (int)result.size() ? ' ' : '\n');
    }

    return 0;
}