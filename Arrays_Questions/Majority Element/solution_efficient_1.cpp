#include <bits/stdc++.h>
using namespace std;
int findCandidate(int arr[], int size){
  int maj_index = 0; int count =1;
  for(int i =1; i<size; i++){
    if(arr[maj_index]== arr[i])
      count++;
    else
      count--;
    if(count == 0){
      maj_index = i;
      count = 1;
    }
  }
  return arr[maj_index];
}

void printMajority(int arr[], int size){
  int result = findCandidate(arr, size);
  int count = 0;
  for(int i=0; i<size; i++){
    if(arr[i] == result)
      count++;
  }
  if(count > size/2){
    cout<<result<<endl;
  }
  else
    cout<<"No Majority element"<<endl;
}

int main() {
  int arr[50];
  int n;
  cin>>n;
  for(int i=0; i<n; i++){
    cin>>arr[i];
  }
  printMajority(arr,n);
  return 0;
}
