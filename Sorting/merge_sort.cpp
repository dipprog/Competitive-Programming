#include<iostream>
using namespace std;
//  Merge procedure to merge to two arrays..
void merge(int *arr, int first,int middle,int last){
	int first_half = middle - first +1; // Finding # of Elements in first half...
	int second_half = last - middle;// Finding # of Elements in second half...
	// Creating two arrays of size (first_half +1) and (second_half + 1) resepectively, 
	// Plus in size for storing INT8_MAX..
	int left_arr[first_half + 1],right_arr[second_half + 1];
	// Storing left half value of the given array into new left_arr..
	for(int i = 0; i< first_half; i++){
		left_arr[i] = arr[first + i];
	}
	// Storing right half value of the given array into new right_arr..
	for(int j = 0; j< second_half; j++){
		right_arr[j] = arr[middle + j + 1];
	}
	// Copying INT8_MAX to last place in both left_array and right_array
	left_arr[first_half] = INT8_MAX;
	right_arr[second_half] = INT8_MAX;
	int i = 0, j=0;
	for(int k = first; k <=last; k++ ){
		if(left_arr[i] <= right_arr[j]){
			arr[k] = left_arr[i];
			i++;
		}
		else{
			arr[k] = right_arr[j];
			j++;
		}
	} 
}
// Merge Sort of a List..Giving first and last index as arguments..
void merge_sort(int *arr,int first,int last){
	if(first < last){
		int middle = (first + last)/2; // finding the middle element..
		merge_sort(arr,first,middle);//Applying Merge Sort on lelf half of the given array
		merge_sort(arr,middle+1,last);// Applying Merge Sort on right half of the given array
		merge(arr,first,middle,last); // And,finally merging the two half using merge procedure..
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
	cout<<"performimg merge_sort"<<endl;
	merge_sort(arr,0,n-1);
	cout<<"Element after sorting"<<endl;
	for(int i =0 ; i< n; i++){
		cout<<arr[i]<<" ";
	}
}
