//
// Created by ML201 on 2/27/2026.
#include <cmath>
#include <iostream>
#include <math.h>
using namespace std;
int main() {

    double x1,y1,x2,y2;
    cout<<"Enter x1:"<<endl;

    cin>>x1;
    cout<<"Enter y1:"<<endl;
    cin>>y1;
    cout<<"Enter x2:"<<endl;
    cin>>x2;
    cout<<"Enter y2:"<<endl;
    cin>>y2;

    double distance = sqrt(pow(x2-x1,2)+pow(y2-y1,2));
    cout<<distance<<endl;
    return 0;

}