//https://leetcode.com/problems/subarray-sum-equals-k/
int subarraySum(vector<int>& nums, int k) {
    size_t sum = 0, res = 0;
    unordered_map<int, int> mp;
    mp[0] = 1;
    for (int n : nums) {
        sum += n;
        if (mp.contains(sum - k)) res += mp[sum - k];
        mp[sum]++;
    }
    return res;
}
