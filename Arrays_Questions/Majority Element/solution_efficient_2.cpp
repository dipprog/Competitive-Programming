#include <bits/stdc++.h>
using namespace std;
void findMajority(int arr[], int size){
  unordered_map<int, int> m;
  for(int i=0; i<size; i++)
    m[arr[i]]++;
  int count = 0;
  for(auto i : m){
    if(i.second > size/2){
      count =1;
      cout<<i.first<<endl;
      break;
    }
  }
  if(count == 0)
    cout<<"No Majority element"<<endl;
}

int main() {
  int arr[50];
  int n;
  cin>>n;
  for(int i=0; i<n; i++){
    cin>>arr[i];
  }
  findMajority(arr,n);
  return 0;
}
