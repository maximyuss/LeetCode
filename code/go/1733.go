// https://leetcode.com/problems/minimum-number-of-people-to-teach/
func minimumTeachings(n int, languages [][]int, friendships [][]int) int {
	m := len(languages)
	learned := make([][]bool, m)
	for i, list := range languages {
		row := make([]bool, n+1)
		for _, x := range list { row[x] = true }
		learned[i] = row
	}

	dumbs := make([]bool, m)
	freq := make([]int, n+1)
	cnt_dumbs := 0

	add := func(u int) {
		if dumbs[u] { return }
		dumbs[u] = true
		cnt_dumbs++
		for _, x := range languages[u] { freq[x]++ }
	}

	for _, friend := range friendships {
		u, v := friend[0]-1, friend[1]-1
		lu := languages[u]
		if len(lu) > len(languages[v]) {
			u, v = v, u
			lu = languages[u]
		}
		shared := false
		for _, x := range lu {
			if learned[v][x] {
				shared = true
				break
			}
		}
		if !shared {
            add(u)
            add(v)
		}
	}

	max := 0
	for i := 1; i <= n; i++ {
		if freq[i] > max { max = freq[i] }
	}
	return cnt_dumbs - max
}
