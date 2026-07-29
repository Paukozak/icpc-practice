#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n;
    cin >> n;

    vector<long long> c(5, 0);
    for (int i = 0; i < n; i++) {
        long long x;
        cin >> x;
        c[x % 5]++;
    }

    long long grupos = 0;

    // 1. Cartas con resto 0 forman un grupo cada una
    grupos += c[0];
    c[0] = 0;

    // 2. Emparejar resto 1 con resto 4
    long long par14 = min(c[1], c[4]);
    grupos += par14;
    c[1] -= par14;
    c[4] -= par14;

    // 3. Emparejar resto 2 con resto 3
    long long par23 = min(c[2], c[3]);
    grupos += par23;
    c[2] -= par23;
    c[3] -= par23;

    // 4. Con lo que sobra, intentar formar combinaciones de 3 o más cartas
    // Nota: Solo puede haber sobrantes en (1 o 4) y en (2 o 3) al mismo tiempo.
    // Ej: Si sobraron de resto 1 y de resto 2:
    // - 2 de resto 2 + 1 de resto 1 = 5
    // - 3 de resto 1 + 1 de resto 2 = 5
    // - 5 de resto 1 = 5
    // - 5 de resto 2 = 5

    // Podemos simular un pequeño Greedy para gastar los sobrantes:
    while (true) {
        if (c[2] >= 2 && c[1] >= 1) { // 2+2+1 = 5
            c[2] -= 2; c[1] -= 1; grupos++;
        } else if (c[1] >= 2 && c[3]>=1){ //3+1+1
            c[1]-=2;c[3]-=1; grupos++;
        } else if (c[2]>=1 && c[4]>=2){ //4+4+2
            c[2]-=1;c[4]-=2; grupos++;
        } else if (c[3] >= 2 && c[4] >= 1) { // 3+3+4 = 10 -> mod 5 = 0
            c[3] -= 2; c[4] -= 1; grupos++;
        } else if (c[1] >= 3 && c[2] >= 1) { // 1+1+1+2 = 5
            c[1] -= 3; c[2] -= 1; grupos++;
        }  else if (c[4] >= 3 && c[3] >= 1) { // 4+4+4+3 = 15 -> mod 5 = 0
            c[4] -= 3; c[3] -= 1; grupos++;
        } else if (c[1]>=1 && c[3]>=3){ // 3+3+3+1 
            c[1]-=1;c[3]-=3;grupos++;
        } else if (c[4]>=1 && c[2]>=3){ //4 + 2 +2 +2
            c[4]-=1;c[2]-=3;grupos++;
        } else if (c[1] >= 5) {
            c[1] -= 5; grupos++;
        } else if (c[2] >= 5) {
            c[2] -= 5; grupos++;
        } else if (c[3] >= 5) {
            c[3] -= 5; grupos++;
        } else if (c[4] >= 5) {
            c[4] -= 5; grupos++;
        } else {
            break; // Ya no se pueden formar más grupos de suma % 5 == 0
        }
    }

    cout << grupos << "\n";

    return 0;
}