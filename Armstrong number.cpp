#include<iostream>
#include<cmath>
#include<math.h>
using namespace std;
int main (){
        int n;
        cin>>n;
        int sum=0;
        int original=n;
        while(n>0){
              int lastdgt=n%10;
              sum+=pow(lastdgt,3);
              n=n/10;
        }
        if(sum==original){
                cout<<"armstrong number";
        }
        else{
                cout<<"not armstrong";
        }
return 0;
}