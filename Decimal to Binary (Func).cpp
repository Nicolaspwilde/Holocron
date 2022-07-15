#include <iostream>
using namespace std;
int bin(int n){
  
  int i=1;
  int rem=0;
  int ans=0;
  while(n>0){
    rem=n%2;
    n=n/2;
    ans= ans+rem*i;
    i=i*10;
  }
  return ans;
}
int main() {
  int n;
  cin>>n;
  cout<<bin(n);
  return 0;
}