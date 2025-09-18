// https://leetcode.com/problems/word-search/
func exist(board [][]byte, word string) bool {
	m, n := len(board), len(board[0])
	if len(word) > m*n { return false }

	w := []byte(word)
	var bc, wc [128]int
	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ { bc[board[i][j]]++ }
	}
	for _, c := range w { wc[c]++ }
	for i := 0; i < 128; i++ {
		if wc[i] > bc[i] {
			return false
		}
	}
	if bc[w[0]] > bc[w[len(w)-1]] {
		for i, j := 0, len(w)-1; i < j; i, j = i+1, j-1 {
			w[i], w[j] = w[j], w[i]
		}
	}

	dirs := [][2]int{{1, 0}, {-1, 0}, {0, 1}, {0, -1}}
	var dfs func(i, j, k int) bool
	dfs = func(i, j, k int) bool {
		if k == len(w) {
			return true
		}
		if i < 0 || i >= m || j < 0 || j >= n || board[i][j] != w[k] { return false }
		cur := board[i][j]
		board[i][j] = '#'
		for _, d := range dirs {
			if dfs(i+d[0], j+d[1], k+1) { return true }
		}
		board[i][j] = cur
		return false
	}

	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			if dfs(i, j, 0) {
				return true
			}
		}
	}
	return false
}
