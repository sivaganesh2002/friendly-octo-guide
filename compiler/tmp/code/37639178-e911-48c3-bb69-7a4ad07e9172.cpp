#include <iostream>
#include <vector>
using namespace std;

int missingNumber(vector<int>& nums) {
    int n = nums.size();
    int expected_sum = n * (n + 1) / 2;
    int actual_sum = 0;
    for (int num : nums) {
        actual_sum += num;
    }
    return expected_sum - actual_sum;
}

int main() {
    int n;
    cin >> n;
    vector<int> nums1;
    
   for(int &r : nums1 ) 
         cin >> r;

    cout << "Missing number: " << missingNumber(nums1) << endl;

    return 0;
}