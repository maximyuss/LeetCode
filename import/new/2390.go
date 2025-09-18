# https://leetcode.com/problems/removing-stars-from-a-string/
func removeStars(s string) string {
	stack := make([]byte, len(s))
	idx := 0
	for i := 0; i < len(s); i++ {
		if s[i] != '*' {
			stack[idx] = s[i]
			idx++
		} else {
			idx--
		}
	}
	return string(stack[:idx])
}
