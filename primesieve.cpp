#include <iostream>
#include <cstring>
#include <bitset>
using namespace std;

#define N 100000010

bitset<N> pp;
int x;

void init(){
    for (int i = 2; i < N; i++) {
        if (pp[i]){
            x = 2 * i;
            while (x < N){
                pp[x] = 0;
                x += i;
            }
        }
    }
}

int sum(int n){
    int count = 0;
    for (int i = 2; i <= n; i++)
        if (pp[i]) count++;
    return count;
}

int main(){
    int n, q, a;
    pp.flip();
    init();
    pp[1] = 0;
    cin >> n >> q;
    cout << sum(n) << endl;
    while (q--){
        cin >> a;
        cout << pp[a] << endl;
    }
    return 0;
}