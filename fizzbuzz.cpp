#include <iostream>

using namespace std;

int main() {
    int n;


    do {
        cout << "Enter a number between 10 and 100 ";
        cin >> n;
    } while (n < 10 || n > 100);


    int fizzCount = 0;
    int buzzCount = 0;
    int fizzBuzzCount = 0;



    for (int i = 1; i <= n; i++) {

        if (i % 7 == 0) {
            cout << i << ": Skipped" << endl;

            continue;
        }


        if (i % 3 == 0 && i % 5 == 0) {
            cout << "FizzBuzz" << endl;
            fizzBuzzCount++;
        }

        else if (i % 3 == 0) {
            cout << "Fizz" << endl;
            fizzCount++;
        }

        else if (i % 5 == 0) {
            cout << "Buzz" << endl;
            buzzCount++;
        }

        else {
            cout << i << endl;
        }
    }


    cout << "\n--- summary ---" << endl;
    cout << "Fizz Count: " << fizzCount << endl;
    cout << "Buzz Count: " << buzzCount << endl;
    cout << "FizzBuzz Count: " << fizzBuzzCount << endl;

    return 0;
}
