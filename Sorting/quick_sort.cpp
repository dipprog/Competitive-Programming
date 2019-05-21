#include<iostream>
using namespace std;

// partitioning the array (finding an element correct position in the array)..
int partition(int *arr, int first,int last){
	int pivot = arr[last]; // Pivot element (partioning element taken as last elenment in the array in this case)..
	int i = first -1; // initially i is pointing to no element in the partition..
	for(int j=first; j < last; j++){
		if(arr[j] <= pivot ){
			i++;
			int temp = arr[i];
			arr[i] = arr[j];
			arr[j] = temp;
		}
	}
	int temp = arr[i+1];
	arr[i+1] = arr[last];
	arr[last] = temp;

	return (i+1);
}

// Quick Sort Recursive Algorithm

void quick_sort(int *arr, int first,int last){
	if(first < last){
		int pivot_position = partition(arr,first,last);
		quick_sort(arr,first,pivot_position-1);
		quick_sort(arr,pivot_position +1, last);
	}
}

// Driving Program...
int main(){
	int n;
	int arr[100];
	cout<<"Enter the size of array"<<endl;
	cin>>n;
	cout<<"Enter the element"<<endl;
	for(int i =0 ; i< n; i++){
		cin>>arr[i];
	}
	cout<<"performimg quick_sort"<<endl;
	quick_sort(arr,0,n-1);
	cout<<"Element after sorting"<<endl;
	for(int i =0 ; i< n; i++){
		cout<<arr[i]<<" ";
	}
}
