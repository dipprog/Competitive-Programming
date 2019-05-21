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

bool isAlphabet(char x){
	return ( (x >='A' && x <='Z') || (x >='a' && x <='z')  );
}

int main(){

	char a[] = "Ab,c,de!$";
	int size = sizeof(a)/sizeof(a[0]);
	char temp[size];
	int j =	0;
	for(int i=0; i< size; i++){
		if(isAlphabet(a[i])){
			temp[j++] = a[i];
		}
	}
	temp[j] = '\0';
	int size_temp = j;
	//cout<<temp<<endl;
	printArray(a,size);
	reverseArray(temp,0,size_temp-1);
	//cout<<temp<<endl;
	j=0;
	for(int i=0; i<size; i++){
		if(isAlphabet(a[i])){
			a[i]=temp[j];
			j++;
		}
	}
	printArray(a,size);
	return 0;
}
