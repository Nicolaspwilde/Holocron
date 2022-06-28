#include<iostream>
#include<bits/stdc++.h>
using namespace std;


void Merge(int arr[], int low, int mid, int high){
 // Merge Routine code here

 int temp[100]; // auxiliary array
 int start=low;
 int q=mid+1;
 int l=low;
 int k=0;
 while(low<=mid && q<=high){
     if(arr[low] <= arr[q]){
         temp[k++]=arr[low++];
     }
     else{
         temp[k++]=arr[q++];
     }
 }
 // if in left half i reaches more than mid  &  elements in right half  is still to traverse
  
 if(low>mid){
     for(;q<=high;){
         temp[k++]=arr[q++];
     }
 }
 // if in right half q reaches greater high &  elements in left half  is still to traverse
 else{
     for(;low<=mid;){
     temp[k++]=arr[low++];
     }
 }

//  copy back to array arr
for(l=start;l<=high;l++){
    arr[l]=temp[l];
}

}
void MergeSort(int arr[],int low, int high ){
      // Divide and Conquer
     if(low>=high){
       return; 
       }
     int mid= (low+high)/2;
     MergeSort(arr, low, mid);          // decompose
     MergeSort(arr, mid+1, high);      // decompose
     Merge(arr, low, mid , high);     // recompose


}



int main(){
    int N;
    cin>>N;
    int arr[N];

    for(int i=0;i<=N-1;i++){
        cin>>arr[i];
    }
     MergeSort(arr, 0 ,N-1);
     cout<<"After Sorting:"<<endl;
     
       for(int i=0;i<=N-1;i++){
        cout<<arr[i]<<"  ";
    }
  return 0;
}
