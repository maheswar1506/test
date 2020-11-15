#include<bits/stdc++.h>
using namespace std;

void print_post_order(int pre[],int n,int min_val,int max_val,int &pre_order_index)
{
    if(pre_order_index ==n)
    {
        return;
    }
    if(pre[pre_order_index] < min_val or pre[pre_order_index] > max_val)
    {
        return;
    }
    int root_data = pre[pre_order_index];
    pre_order_index++;
    print_post_order(pre,n,min_val,root_data,pre_order_index);
    print_post_order(pre,n,root_data,max_val,pre_order_index);
    cout<<root_data<<" ";
}

void post_order(int pre[],int n)
{
    int pre_order_index = 0;
    print_post_order(pre,n,INT_MIN,INT_MAX,pre_order_index);
}

int main()
{
    int pre[] = { 40, 30, 35, 80, 100 }; 
    int n = sizeof(pre) / sizeof(pre[0]);
    post_order(pre,n);
}
