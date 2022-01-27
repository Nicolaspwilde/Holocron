#include <iostream>
using namespace std;
int main()
{
    char button;
    cout<<"Enter the button choice";
    cin>> button;
    switch (button)
    {

    case 'a':
        cout<<"hola"<<endl;
        break;

    case 'b':
        cout<<"namaste"<<endl;
        break;
            
    case 'c':
        cout<<"hi"<<endl;
        break;           

    default:
    cout<<"learning"<<endl;
            break;
    }

    return 0;



}