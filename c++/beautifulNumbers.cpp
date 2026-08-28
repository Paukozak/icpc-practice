//https://codeforces.com/problemset/problem/300/C

#include <bits/stdc++.h>
typedef long long ll;

using namespace std;
// El módulo típico en programación competitiva
const int MOD = 1e9 + 7;
// El tamaño máximo de N que esperas en el problema (ej. 100,000)
const int MAX = 1000005; 


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


// 5. CALCULAR PERMUTACIONES (nPr)
// Fórmula: n! / (n-r)!
long long nPr(int n, int r) {
    if (r < 0 || r > n) return 0;
    long long numerador = fact[n];
    long long denominador = inversoModular(fact[n - r]);
    
    return (numerador * denominador) % MOD;
}

bool es(long long x, long long a, long long b) {

    while (x > 0) {
        int digito_actual = x % 10; 
        if (digito_actual != a && digito_actual != b) {
            return false;
        }  
        x /= 10; 
    }
    return true; 
}



int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    ll a, b, n, suma, total, result;

    cin>>a>>b>>n;

    precalcularFactoriales();

    total=0;

    for (ll i=0; i<=n; i++) {
        suma=(i*a)+(n-i)*b;

        result=es(suma,a,b);

        if (result==true) {
            total+=(nCr(n, i)%MOD);
        }
        
    }

    cout<<total%MOD;

    return 0;
}