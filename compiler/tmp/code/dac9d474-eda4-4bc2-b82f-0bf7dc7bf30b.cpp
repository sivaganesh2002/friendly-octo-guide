#include <iostream>
#include <vector>

int missingNumber(std::vector<int>& nums) {
    int n = nums.size();
    int expected_sum = (n * (n + 1)) / 2;
    int actual_sum = 0;
    for (int num : nums) {
        actual_sum += num;
    }
    return expected_sum - actual_sum;
}

int main() {
    int n;
    std::cin >> n; // Number of elements in the array

    std::vector<int> nums(n);
    for (int i = 0; i < n; ++i) {
        std::cin >> nums[i];
    }

    int result = missingNumber(nums);
    std::cout << result << std::endl;

    return 0;
}