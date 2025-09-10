// https://leetcode.com/problems/number-of-people-aware-of-a-secret/
func peopleAwareOfSecret(n int, delay int, forget int) int {
	const MOD = 1000000007
	memo := make([]int, n)
	memo[0] = 1
	calc := 0
	for day := delay; day != n; day++ {
		calc += memo[day-delay]
		if day >= forget {
			calc -= memo[day-forget]
		}
		memo[day] = calc % MOD
	}
	res := 0
	for day := n - forget; day != n; day++ {
		res = (res + memo[day]) % MOD
	}
	return res
}
