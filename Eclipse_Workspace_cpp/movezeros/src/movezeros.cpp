/*
 * Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.
 *
 * Example:
 *
 * Input: [0,1,0,3,12]
 * Output: [1,3,12,0,0]
 */

#include <string>
#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        // j - index to processed non-zero element
        unsigned int j = 0;
        // move all the nonzero elements advance
        // i - index to processing element
        for (unsigned int i = 0; i < nums.size(); i++) {
            // Copy the non-zero element to proper location
            if (nums[i] != 0) {
                nums[j] = nums[i];
                j++;
            }
        }
        // Set the tail elements to zero
        for (;j < nums.size(); j++) {
            nums[j] = 0;
        }
    }
};

int main() {
    vector<int> test_vector{1,0,2,3,0,4,5};

    cout << "before: ";
    for (int x : test_vector)
        cout << x << " ";
    cout << endl;

    Solution().moveZeroes(test_vector);

    cout << endl << "after: ";
    for (int x : test_vector)
        cout << x << " ";

    return 0;
}
