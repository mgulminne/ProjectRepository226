#include <iostream>
using namespace std;

int* createArray(int size) {
    int* arr = new int[size];
    return arr;
}
void swapValues(int*p1, int*p2) {
    int temp = *p1;
    *p1 = *p2;
    *p2 = temp;
}


void printArray(int*arr, int size) {
    for (int i = 0; i < size; i++) {
        cout << *(arr + i) <<"";
    }
    cout << endl;
}
int findMax(int* arr, int size) {
    int maxVal= *arr;
    for (int i =0;i < size; i++){
        if(*(arr + i) > maxVal) {
            maxVal = *(arr + i);
        }
    }
    return maxVal;
}
void reverseArray(int*arr,int size){
    int* start = arr;
    int* end = arr +(size -1);
    while(start < end) {
        swapValues(start, end);
        start++;
        end--;
    }
}

void deleteArray(int*arr) {
    delete[] arr;
    cout<<"Memory released successfully "<<endl;
}




int main() {
    int size;
    cout << "Creating dynamic array... ";
    cout << "Enter the size of the array" << endl;
    cin >> size;

    int* arr = createArray(size);

    cout << "Enter the elements of the array" << endl;
    for (int i = 0; i < size; i++) {
        cin >> *(arr + i);
    }

    cout<< "Array elements" << endl;
    printArray(&*arr, size);
    cout<<"Maximum value is "<<findMax(arr, size) << endl;
    cout<<"---------------------------------" << endl;
    cout<<"Swapping two numbers"<<endl;
    int a =5,b =8;
    cout<<" before swapping "<<endl;cout<<a<<" "<<b<<endl;
    swapValues(&a,&b);
    cout<<"After swapping "<<endl;
    cout<<a<<" "<<b<<endl;


    cout<<"---------------------------------"<<endl;
    cout<<"Reversing Array"<< endl;
    reverseArray(arr, size);
    cout<<"After reversing "<<endl;
    printArray(arr, size);


    cout<<"------------------------------"<<endl;
    cout<<"Deleting the array"<<endl;

    deleteArray(arr);
    return 0;

}



