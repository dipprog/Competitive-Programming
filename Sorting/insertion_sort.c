#include<stdio.h>

/*
void swap(int *a , int *b){
  int temp;
  temp = *a;
  *a = *b;
  *b = temp;
}*/
void insertion_sort(int arr[], int size){
  int i;
  int temp;
  for(i=0; i<size; i++){
    temp = arr[i];
    int j;
    j = i;
    while(j>0 && temp < arr[j-1]){
      arr[j] = arr[j-1];
      j = j-1;
    }
    arr[j] = temp;
  }
}

int main(){
  int arr[20];
  int size,i,test;
  printf("Enter the number of test case:\n");
  scanf("%d",&test);
  while(test--){
    printf("Enter the size of array:\n");
    scanf("%d",&size);
    printf("Enter the element of the array:\n");
    for(i=0; i< size; i++){
      scanf("%d",&arr[i]);
    }
    insertion_sort(arr, size);
    printf("Array after sorting:\n");
    for(i=0; i< size; i++){
      printf("%d  ",arr[i]);
    }
    printf("\n");
  }
  return 0;
}
