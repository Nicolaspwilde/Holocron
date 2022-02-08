#include <iostream>
using namespace std;
int main()
{
    int n1,n2;
    cout<<"Enter the number1";
    cin>>n1;
    cout<<"Enter the number2";
    cin>>n2;
    char symbol;
    cout<<"Enter the operator";
    cin>>symbol;
    switch(symbol)
    {
        case '+':
            cout<<n1+n2<<endl;
            break;
        case '-':
            cout<<n1-n2<<endl;
            break;
        case '*':
            cout<<n1*n2<<endl;
            break;
        case '/':
            cout<<n1/n2<<endl;
            break;
        default:
            cout<<"enter another operator"<<endl;
            break;
    }

return 0 ;



}