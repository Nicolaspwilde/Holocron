#include <iostream>
using namespace std;
int main()
{
  cout<<"Enter a number: "; int check; cin>>check;
  //checking whether the number is even or odd
  if(check % 2 == 0)
  {
    cout<<check<<" is an even number";
  }
  else
  {
     cout<<check<<"is an odd number";
  }
  return 0;
}