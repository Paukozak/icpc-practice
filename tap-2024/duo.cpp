#include <iostream>

using namespace std;

int main () {
    ios::sync_with_stdio(0); 
    cin.tie(0);
    int a, b, c;
    cin>>a>>b>>c;

    if ((a+b)<=c) {
        cout<<"S";
    }
    
    else if ((a+c)<=b) {
        cout<<"S";
    }
    
    else if ((c+b)<=a) {
        cout<<"S";
    }
    else {
        cout<<"N";
    }

    return 0;
}