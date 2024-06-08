//https://leetcode.com/problems/continuous-subarray-sum/
bool checkSubarraySum(vector<int>& nums, int k) {
	unordered_map<int, int> mp;
	mp[0] = -1;
	size_t sum = 0, rem;
	for (int i = 0; i < nums.size(); i++) {
		sum += nums[i];
		rem = sum % k;
		if (mp.contains(rem)) {
			if (i - mp[rem] > 1)
				return true;
		}
		else
			mp[rem] = i;
	}
	return false;
}
