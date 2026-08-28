//https://codeforces.com/problemset/problem/459/B

#include <bits/stdc++.h>
using namespace std;

// El módulo típico en programación competitiva
const int MOD = 1e9 + 7;
// El tamaño máximo de N que esperas en el problema (ej. 100,000)
const int MAX = 200005; 


vector<long long> fact(MAX);


// 1. PRECALCULAR FACTORIALES
// Hacemos esto una sola vez al inicio del programa. Toma O(N).
void precalcularFactoriales() {
    fact[0] = 1;
    for (int i = 1; i < MAX; i++) {
        fact[i] = (fact[i - 1] * i) % MOD;
    }
}


// 2. EXPONENCIACIÓN BINARIA (Rápida)
// Calcula (base^exp) % MOD en tiempo O(log exp).
long long power(long long base, long long exp) {
    long long res = 1;
    base %= MOD;
    while (exp > 0) {
        if (exp % 2 == 1) res = (res * base) % MOD;
        base = (base * base) % MOD;
        exp /= 2;
    }
    return res;
}


// 3. INVERSO MULTIPLICATIVO MODULAR
// Como NO podemos usar división normal (/) con módulos, 
// usamos el Pequeño Teorema de Fermat para "dividir".
long long inversoModular(long long n) {
    return power(n, MOD - 2);
}

// 4. CALCULAR COMBINACIONES (nCr)
// Fórmula: n! / (r! * (n-r)!)
long long nCr(int n, int r) {
    if (r < 0 || r > n) return 0;
    long long numerador = fact[n];
    
    // En lugar de dividir, multiplicamos por los inversos modulares
    long long denominador = (inversoModular(fact[r]) * inversoModular(fact[n - r])) % MOD;
    
    return (numerador * denominador) % MOD;
}



typedef long long ll;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    precalcularFactoriales();

    ll n, fb, fs;
    cin>>n;
    vector<ll> beauty(n);

    for (ll i=0; i<n; i++) {
        cin>>beauty[i];
    }
    
    ll smaller = *min_element(beauty.begin(), beauty.end());   
    ll bigger = *max_element(beauty.begin(), beauty.end());  

    map<ll, ll> freq;

    for (ll x : beauty) {
        freq[x]++;
    }

    fb=freq[bigger];
    fs=freq[smaller];

    if (smaller==bigger) {
        cout<<(bigger-smaller)<<" "<<n * (n - 1) / 2;
    } else {
        cout<<(bigger-smaller)<<" "<<((fb*fs));
    }

    return 0;
}