#include <iostream>
using namespace std;

int main ()
{
int n;
cin>>n;
int i=1;
for(;i<=n;i++){
        int j=1;
        for(;j<=n-i;j++){
                cout<<" ";
                }
        int k;
        k=i;
        for(;j<=n;j++){
                cout<<k--<<" ";
                }
        k=2;
        for(;j<=n+i-1;j++){
                cout<<k++<<" ";
                }       
                cout<<endl;
                }
                return 0;
}
