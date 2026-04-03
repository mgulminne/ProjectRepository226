#include <iostream>


using namespace std;

double calculatePower(double base, int exp) {
    if (exp == 0) return 1;
    return base * calculatePower(base, exp - 1);
}

double calculateGn(double r, int n) {
    if (n == 0) return 1;
    return calculatePower(r, n) + calculateGn(r, n - 1);
}

int main() {
    double r;
    int n;

    cout << "Enter n: ";
    cin >> n;
    cout << "Enter r: ";
    cin >> r;

    double result = calculateGn(r, n);
    cout << "Gn = " << result << endl;

    return 0;
}
