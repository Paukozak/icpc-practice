// https://codeforces.com/gym/106682/problem/C
#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

const ll INF = 2e18; // numero muy grande para arrancar la comparación

int n;
vector<ll> A, B;

// Tablas de memoización
vector<ll> memoA, memoB;
vector<ll> memoSufA, memoSufB;
vector<bool> visA, visB, visSufA, visSufB;

// Declaración de funciones recursivas
ll get_sufMaxA(int x);
ll get_sufMinB(int x);

// Valor si Agustín avanza a la posición x (ahora es turno de Brian)
ll playAgustin(int x)
{
    if (visA[x])
        return memoA[x];
    visA[x] = true;

    // 1. Si Brian decide pasar:
    // Agustín se queda con el puntaje A[x], a menos que a Agustín le convenga avanzar más adelante a algún índice y > x (get_sufMaxA(x + 1)).
    ll si_brian_pasa = max(A[x], get_sufMaxA(x + 1));

    // 2. Si Brian decide avanzar a algún índice y > x:
    // Brian buscará minimizar el puntaje final entre las opciones y > x.
    ll si_brian_avanza = get_sufMinB(x + 1);

    // Brian elige la mejor opción para él (minimizar)
    return memoA[x] = min(si_brian_pasa, si_brian_avanza);
}

// Valor si Brian avanza a la posición x (ahora es turno de Agustín)
ll playBrian(int x)
{
    if (visB[x])
        return memoB[x];
    visB[x] = true;

    // 1. Si Agustín decide pasar:
    // Brian se queda con B[x], a menos que a Brian le convenga
    // avanzar más adelante a algún índice y > x (get_sufMinB(x + 1)).
    ll si_agustin_pasa = min(B[x], get_sufMinB(x + 1));

    // 2. Si Agustín decide avanzar a algún índice y > x:
    // Agustín buscará maximizar el puntaje final entre las opciones y > x.
    ll si_agustin_avanza = get_sufMaxA(x + 1);

    // Agustín elige la mejor opción para él (maximizar)
    return memoB[x] = max(si_agustin_pasa, si_agustin_avanza);
}

// Función recursiva para obtener el máximo que puede lograr Agustín en el rango [x, N]
ll get_sufMaxA(int x)
{
    if (x > n)
        return -INF;
    if (visSufA[x])
        return memoSufA[x];
    visSufA[x] = true;

    // Agustín puede elegir x (playAgustin) o elegir algún índice posterior (get_sufMaxA(x + 1))
    return memoSufA[x] = max(playAgustin(x), get_sufMaxA(x + 1));
}

// Función recursiva para obtener el mínimo que puede lograr Brian en el rango [x, N]
ll get_sufMinB(int x)
{
    if (x > n)
        return INF;
    if (visSufB[x])
        return memoSufB[x];
    visSufB[x] = true;

    // Brian puede elegir x (playBrian) o elegir algún índice posterior (get_sufMinB(x + 1))
    return memoSufB[x] = min(playBrian(x), get_sufMinB(x + 1));
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    if (!(cin >> n))
        return 0;

    A.resize(n + 1);
    B.resize(n + 1);

    for (int i = 1; i <= n; ++i)
        cin >> A[i];
    for (int i = 1; i <= n; ++i)
        cin >> B[i];

    memoA.assign(n + 2, 0);
    memoB.assign(n + 2, 0);
    memoSufA.assign(n + 2, 0);
    memoSufB.assign(n + 2, 0);

    visA.assign(n + 2, false);
    visB.assign(n + 2, false);
    visSufA.assign(n + 2, false);
    visSufB.assign(n + 2, false);

    // Estado inicial: x = 0, puntaje s = 0. Agustín comienza el juego:
    // Opción 1: Agustín pasa.
    // Turno de Brian con 1 pase acumulado: Brian puede pasar (termina el juego con s = 0)
    // o avanzar a algún y >= 1 (obteniendo get_sufMinB(1)). Brian minimiza:
    ll si_agustin_pasa = min(0LL, get_sufMinB(1));

    // Opción 2: Agustín avanza a algún índice y >= 1. Agustín maximiza:
    ll si_agustin_avanza = get_sufMaxA(1);

    // Agustín toma la decisión que maximice su resultado final:
    ll ans = max(si_agustin_pasa, si_agustin_avanza); // agustin no va a saber si tiene que pasar en su primer jugada hasta no saber qué puede elegir Brian después de él

    cout << ans << "\n";
    return 0;
}