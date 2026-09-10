#include <iostream>
using namespace std;

int mixColor(int c1, int c2) {
    return (c1 + c2) / 2;
}

void mixRGB(int r1, int g1, int b1,
           int r2, int g2, int b2,
           int &rMix, int &gMix, int &bMix) {

    rMix = mixColor(r1, r2);
    gMix = mixColor(g1, g2);
    bMix = mixColor(b1, b2);
}

int main() {
    int r1, g1, b1;
    int r2, g2, b2;

    cin >> r1 >> g1 >> b1;
    cin >> r2 >> g2 >> b2;

    int rMix, gMix, bMix;

    mixRGB(r1, g1, b1, r2, g2, b2,
           rMix, gMix, bMix);

    cout << rMix << " " << gMix << " " << bMix;

    return 0;
}
