#include<bits/stdc++.h>
using namespace std;
void reverseArray(char arr[], int start, int end){
	while(start < end){
		swap(arr[start], arr[end]);
		start++;
		end--;
	}	
}

void printArray(char arr[], int size){
	for(int i=0; i<size; i++){
		cout<<arr[i]<<" ";
	}
	cout<<endl;
}

int main(){

	char a[] = "holiday night";
	int size = sizeof(a)/sizeof(a[0]);
	printArray(a,size);
	reverseArray(a,0,size -1);
	printArray(a,size);
	return 0;
}
