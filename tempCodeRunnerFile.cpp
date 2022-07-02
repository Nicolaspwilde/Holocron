#include <iostream>
using namespace std;

int main()
{
    int num;
    cin>>num;
    
    if (num > 0)
        cout << "The number is positive";
    else if (num < 0)
        cout << "The number is negative";
    else
        cout << "Zero";
    
    return 0;
}


#include<iostream>
using namespace std;

int main()
{
    int num = -12;
    if (num >= 0)
    {
        if (num == 0)
            cout << "Zero";
        else
            cout << "The number is positive";
    }
    else
            cout << "The number is negative";
    
    return 0;
}