#include<iostream>
#include<math.h>
using namespace std;
bool pyt(int x,int y,int z){
        
        int a = max(x,max(y,z));
        int b,c;
        if (a==x){
                b=y;
                c=z;
        }
        else if (a==y)
        {
                b=x;
                c=z;
        }
        else {
                b=y;
                c=x;
        }
        if((a*a) == ((b*b) + (c*c)))
                return true;
        
        else
                return false;
        
        return pyt;
}

int main(){
    int x,y,z;
    cin>>x>>y>>z;
    if(pyt(x,y,z)){
        cout<<"pythagorean triplet"<<endl;
    }
    else{
        cout<<"not a pythagorean triplet"<<endl;
    }
    return 0;
}

