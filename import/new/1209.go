// https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/
func removeDuplicates(s string, k int) string {
	type pair struct { c byte; v int }
	stack := make([]pair, 0, len(s))
	for i := 0; i < len(s); i++ {
		n := len(stack)
		if n > 0 && stack[n-1].c == s[i] {
			stack[n-1].v = (stack[n-1].v + 1) % k
			if stack[n-1].v == 0 { stack = stack[:n-1] }
		} else { 
			stack = append(stack, pair{s[i], 1})
		}
	}
	res := make([]byte, 0, len(s))
	for _, cnt := range stack {
		for i := 0; i < cnt.v; i++ { res = append(res, cnt.c) }
	}
	return string(res)
}
