#include <iostream>
using namespace std;
int main() 
{ 
    
    int Number, N, Sum;
    
    cout<<"\n Kindly Insert an Integer Variable\n"; 
    cin>>N;

    {
       Sum = (N*(N+1))/2;
    }

    //display
    cout<<"Sum of Natural Numbers: "<< Sum;

    return 0;
}