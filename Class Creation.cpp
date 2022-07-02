#include<iostream>
using namespace std;

class Rectangle{
    public:
    int Length, Breath;
    char nameofStudent[20];
    int area(){
    return Length*Breath;

    }

};
int main()
{
    Rectangle rectObj;
    rectObj.Length = 10;
    rectObj.Breath = 20;

    cout<< "The area of Rectangle is:"<<rectObj.area()<< endl;

    return 0;
}