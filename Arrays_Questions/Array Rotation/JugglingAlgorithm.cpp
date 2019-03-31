#include <iostream>
using namespace std;
int gcd(int a,int b){
	if(b == 0){
		return a;
	}
	else
		return gcd(b,a%b);
}
void ArrayRotationJugglingAlgorithm(int arr[], int size, int d){
	int tempVariable,cycleCounter,innerIndexPointer, shifting=-1;
	for(cycleCounter = 0; cycleCounter< gcd(size,d);cycleCounter++){
    tempVariable = arr[cycleCounter];
		innerIndexPointer = cycleCounter;
		while(1){
			shifting = (innerIndexPointer + d)%size;
			if(shifting == cycleCounter)
				break;
			arr[innerIndexPointer] = arr[shifting];
			innerIndexPointer = shifting;
		}
		arr[innerIndexPointer] = tempVariable;
	}
}
void displayArray(int arr[],int size){
  for(int i=0; i<size; i++){
    cout<<arr[i]<<" ";
  }
  cout<<endl;
}

int main(){
  int n,i,d;
  cout<<"Enter size of the Array\n";
  cin>>n;
  int A[n];
  cout<<"Enter Array elements\n";
  for(i=0;i<n;i++)
   cin>>A[i];
  cout<<"Enter the value of d\n";
  cin>>d;
  displayArray(A,n);
  ArrayRotationJugglingAlgorithm(A,n,d);
  displayArray(A,n);
  return 0;
}
// Time complexity : O(n)
// Auxiliary Space : O(1)
