#include<iostream>
#include<math.h>
using namespace std;

int main()
{
    int num1;
    int num2;
    num1=0;
    num2=1;
    int num;
    cin>>num;
        for(int i=1;i<=num;i++){
                int fib= num1+num2;
                num1=num2;
                num2=fib;
                cout<<num1<<endl;

        }

return 0;
}

