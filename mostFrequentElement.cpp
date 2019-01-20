#include<bits/stdc++.h>
using namespace std;

int mostFrequent(int arr[], int size){
  // Insert all elements in hash
  unordered_map<int, int> hash;
  for(int i=0; i< size; i++){
    hash[arr[i]]++;
  }

  // Find most frequent element
  int max_count = 0,result = -1;
  for(auto i : hash){
    if( max_count < i.second){
      result = i.first;
      max_count = i.second;
    }
  }
  return result;
}

int main(){
  int n;
  int arr[100];
  cin>>n;
  for(int i=0; i<n; i++){
    cin>>arr[i];
  }
  int result = mostFrequent(arr, n);
  cout<<"The most frequent element is : "<<result<<endl;
  return 0;
}

// Time complexity : O(n)
// Space complexity : O(n)
