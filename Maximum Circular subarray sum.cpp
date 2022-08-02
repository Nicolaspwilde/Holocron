#include<bits/stdc++.h>
#include<climits>
#include<iostream>
using namespace std;

int kadane(int a[],int n){
int curr_sum = 0;
int max_sum = INT_MIN;
for(int i=0;i<n;i++){
  curr_sum = curr_sum + a[i];
  if(curr_sum<0){
    curr_sum=0;
  }
  max_sum = max(max_sum,curr_sum);
  }
  return max_sum;
}

int main()
{
  int n;
  cin>>n;
  int a[n];
  for(int i=0;i<n;i++)
  {
    cin>>a[i];
  }
int wrapsum;
int nonwrapsum;
nonwrapsum = kadane(a,n);
int totalsum=0;
for(int i=0;i<n;i++){
  totalsum+=a[i];
  a[i]=-a[i];
}
wrapsum = totalsum + kadane(a,n);
cout<<max(wrapsum,nonwrapsum)<<endl;
return 0;
}

