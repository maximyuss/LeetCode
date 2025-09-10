// https://leetcode.com/problems/minimum-operations-to-make-the-integer-zero
func makeTheIntegerZero(num1 int, num2 int) int {
    if num1 == 0 { return 0 }
	for k := 1; ; k++ {
		x := int64(num1) - int64(num2)*int64(k)
		if x < int64(k) { return -1 }
		if bits.OnesCount64(uint64(x)) <= k { return k }
	}
}
