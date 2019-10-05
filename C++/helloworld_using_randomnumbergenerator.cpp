#include <bits/stdc++.h>
using namespace std;
int main(){
    vector<vector<char>> matrix;
    string str="Hello World";
    for(int i=0;i<str.length();i++)
    {
    char ch=str[i];
    vector<char> v;
    for(int j=0;j<10;j++)
    {
     v.push_back(ch);
    }
    matrix.push_back(v);
    }
    string final_str="";
    int random_index=rand()%10;
    //cout<<random_index<<"\n";
    for(int i=0;i<str.length();i++)
    {
      // cout<<matrix[i][random_index]<<"\n";
      final_str+=matrix[i][random_index];  
    }
    cout<<final_str;
    
}
