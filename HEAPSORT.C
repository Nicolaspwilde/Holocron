#include<stdio.h>

void HeapSort(int*,int);
void Heapify(int*,int i,int);
void swap(int*,int*);
void BuildMaxHeap(int*,int);

int Input(int a[]){
	int max,i=0;
	printf("\nInput total number of elements:");
	scanf("%d",&max);
	for(;i<max;++i){
		printf("Input a number[%d/%d]:",i+1,max);
		scanf("%d",&a[i]);
	}
return max;
}
void Print(int a[],int max){
	int i;
	for(i=0;i<max;++i)
        printf("\t%d",a[i]);
}

int main()
{
    int i,a[10];//={4,7,6,3,1,8,9,0,2,5};
    int max;
    max=Input(a);
    printf("\nList  of  elements:  ");
	Print(a,max);
	printf("\nHeap Sort  **START**");
	HeapSort(a,max);
	printf("\nHeap Sort    **END**");
	printf("\nSorted by Heap Sort:");
	Print(a,max);
	return 0;
}
void Heapify(int *a,int i,int n){
    int l,r,max;
    l=2*i+1;
    r=2*i+2;
    max=i;
    if(l<n && a[l]>a[max])   max=l;
    if(r<n && a[r]>a[max])   max=r;
    if(max!=i){
        swap(&a[i],&a[max]);
        Heapify(a,max,n);
    }
}
void swap(int *x,int *y){
	int temp=*x;
	*x=*y;
	*y=temp;
}
void BuildMaxHeap(int *a,int n){
    int i;
    for(i=n/2;i>=0;i--)
        Heapify(a,i,n);
}
void HeapSort(int *a,int n){
    int i;
    BuildMaxHeap(a,n);
    printf("\nAfter BUILD_MAX_HEAP:  ");
	Print(a,n);
    for(i=n-1;i>0;i--){
        swap(&a[0],&a[i]);
        Heapify(a,0,i);
        printf("\nAfter heapify (HeapSize=%d):",i);
        Print(a,i);
    }
}






