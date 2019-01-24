#include <iostream>
using namespace std;
int getPairsCount(int arr[],int n, int sum){
  int count= 0; //Initializing result
  for(int i=0; i<n; i++){
    for(int j=i+1; j<n; j++){
      if(arr[i] + arr[j] == sum)
        count++;
    }
  }
  return count;
}
int main() {
  int arr[40];
  int n;
  cin>>n;
  for(int i=0; i<n; i++)
    cin>>arr[i];
  int sum;
  cin>>sum;
  int result = getPairsCount(arr,n,sum);
  cout<<"Result : "<<result;
  return 0;
}
