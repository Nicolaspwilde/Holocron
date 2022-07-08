#include<iostream>
#include<cmath>
#include<math.h>
using namespace std;
int main (){
        int n;
        cin>>n;
        int rev=0;

        while(n>0){
              int lastdgt=n%10;
              rev=rev*10+lastdgt;
              n=n/10;
        }
        cout<<rev<<endl;
return 0;
}