//digital roots sequence

#include <iostream>

using namespace std;

int main() {
    long long num;
    cout << "enter a number greater than 9 ";
    cin >> num;

    if (num <= 9) {
        cout << "enter a number greater than9" << endl;
        return 1;
    }

    int steps = 0;
    cout << num;

    while (num > 9) {
        long long digit_sum = 0;
        long long temp = num;


        while (temp > 0) {
            digit_sum += temp % 10;
            temp /= 10;
        }

        num = digit_sum;
        steps++;
        cout << " -> " << num;
    }

    cout << "\nfinalvalue " << num << endl;
    cout << "steps taken: " << steps << endl;

    return 0;
}
