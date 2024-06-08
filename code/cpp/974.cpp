//https://leetcode.com/problems/subarray-sums-divisible-by-k/
int subarraysDivByK(vector<int>& nums, int k) {
	int sum = 0, rem = 0, count = 0;
	unordered_map<int, int> mp;
	mp[0] = 1;
	for (int n : nums) {
		sum += n;
		rem = (sum % k + k) % k;
		count += mp[rem]++;
	}
	return count;
}
