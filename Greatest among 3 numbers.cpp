#include <iostream>
#include <conio.h>
#include <math.h>
using namespace std ;
int main ()
{
  long long int a,b,c;
    cout<<"Enter the numbers";
    cin>>a>>b>>c;
    if (a>b){

       if(a>c){
            cout<<a<<endl;
       }
        else{
            cout<<c<<endl;
       }
    }
    
    else{
        if(b>c){
            cout<<b<<endl;
        }
        else{
            cout<<c<<endl;
        }
    }

    return 0;

}