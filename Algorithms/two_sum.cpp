class Solution {
public:
	vector<int> twoSum(vector<int>& nums, int target) {
		int len = nums.size();
		vector<int> ret_vector(2);
		//vector<int> ret_vector = [0, 0];
		for (int i = 0; i < len - 1; i++) {
			for (int j = i + 1; j < len; j++) {
				if (nums[i] + nums[j] == target) {
					ret_vector[0] = i;
					ret_vector[1] = j;
					break;
				}
			}
		}
		return ret_vector;
	}
};
