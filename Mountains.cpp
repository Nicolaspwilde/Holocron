#include<iostream>
using namespace std;
int main ()
{
int n;
cin>>n;
for(int i=1;i<=n;i++){
        for(int j=1;j<=n-i;j++){
                if((i+j)%4==0||(i==2 && j%4==0)){
                        cout<<" * ";
                }
                
        }
        cout<<endl;
}
return 0;
}