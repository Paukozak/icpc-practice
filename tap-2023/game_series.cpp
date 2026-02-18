#include <iostream>

using namespace std;

int main () {
    ios::sync_with_stdio(0);
    cin.tie(0);
    int a1,p1,a2,p2;
    cin>>a1>>p1;
    cin>>a2>>p2;

    if ((a1+a2)<(p1+p2)){
        cout<<"P";
    } else if ((a1+a2)>(p1+p2)){
        cout<<"A";
    } else{
        cout<<"D";
    }

    return 0;
}