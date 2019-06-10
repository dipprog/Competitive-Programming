#include<iostream>
using namespace std;

void selection_sort(int arr[], int size){
  // Variable to store the index of minimum value in a list
  int minimum_index;
  for(int i=0; i<size-1; i++){
    // Assuing i to be minimum index initially
    minimum_index=i;
    // Finding minimum index in the sub list
    for(int j=i+1; j<size; j++){
      if(arr[j] < arr[minimum_index])
        minimum_index= j;
    }
    // Putting minimum_value in its correct position 
    swap(arr[i],arr[minimum_index]);
  }
}

int main() {
  int arr[10] = {101,100,34,1,2,3,67,200,201,5};
  selection_sort(arr,10);
  for(int i=0; i< 10; i++){
    printf("%d  ",arr[i]);
  }
  printf("\n");
  return 0;
}
