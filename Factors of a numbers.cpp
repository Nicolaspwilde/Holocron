//Write a program for factorization of 2 number//
#include <iostream>
using namespace std;
int main(){
int a,b;
cin>>a>>b;
int fact1=1;
for(int i=2;i<a;i++){
        fact1= i*a;

}
int fact2=1;
for(int i=2;i<b;i++){
        fact2= i*b;

}
cout<<fact1<<"  "<<fact2<<endl;
return 0;
}