//
// Created by ML201 on 2/27/2026.
#include <iostream>
using namespace std;
int main() {
    int totaSecond;
    cout<< "enter total number";
    cin>>totaSecond;

    int hours = totaSecond / 3600;
    int remainingSec = totaSecond % 3600;
    int minutes = remainingSec / 60;
    int seconds = remainingSec % 60;

    cout<<hours<<":"<<minutes<<":"<<seconds;
    return 0;
}