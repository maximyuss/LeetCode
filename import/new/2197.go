// https://leetcode.com/problems/replace-non-coprime-numbers-in-array/
func gcd(a, b int) int {
	for b != 0 {
		a, b = b, a%b
	}
	return a
}

func replaceNonCoprimes(nums []int) []int {
	stack := make([]int, 0, len(nums))
	for _, a := range nums {
		for a > 1 && len(stack) > 0 {
			n := len(stack) - 1
			b := stack[n]
			gcd_ := gcd(a, b)
			if gcd_ == 1 { break }
			a = a / gcd_ * b
			stack = stack[:n]
		}
		stack = append(stack, a)
	}
	return stack
}
