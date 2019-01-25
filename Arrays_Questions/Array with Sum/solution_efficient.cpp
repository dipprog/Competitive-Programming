#include <bits/stdc++.h>
using namespace std;
int getPairsCount(int arr[],int n, int sum){
  unordered_map<int , int> m;
  
  for(int i=0; i<n; i++)
    m[arr[i]]++;

  int twice_count=0;

  for(int j=0 ; j<n; j++){
    twice_count += m[sum-arr[j]];
    if(sum-arr[j] == arr[j])
      twice_count--;
  }
  return twice_count/2;
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
