#include <iostream>
using namespace std;
int main()
{
        int n;
        cout<<"enter the number";
        cin>>n;

        if(n%2==0 && n%3==0){
            cout<<"the number is divisible by both"<<endl;
        }
        else if (n%2==0)
        {
            cout<<"divisible by 2";
        }
        else if (n%3==0)
        {
            cout<<"divisible by 3";
        }
        else
        {
            cout<<"not divisible by none";
        }

return 0;


}