#include<bits/stdc++.h>

using namespace std;

bool sumofdigit(int arr[],int n,int k){
  int low=0;
  int high=0;
  while (low<high){
    if(arr[low]+arr[high]==k){
      cout<<low<<" "<<high<<endl;
      return true;
    }
    else if(arr[low]+arr[high]>k){
      high--;
    }
    else(arr[low]+arr[high]<k){
      low++;
    }
  }

return false;
}
int main(){
  int arr[] ={2,4,7,11,14,16,20,21};
  int k=31;
  int n;
  cout<<pairsum(arr,n,k)<<endl;
  return 0;
}