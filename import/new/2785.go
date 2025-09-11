// https://leetcode.com/problems/sort-vowels-in-a-string
var vowels = []byte("AEIOUaeiou")
var idx [128]int8

func init() {
    for i, c := range vowels { idx[c] = int8(i) + 1 }
}

func sortVowels(s string) string {
    b := []byte(s)

	var counts [10]int
	for _, c := range b {
		k := idx[c] - 1
		if k >= 0 { counts[k]++ }
	}

	res := make([]byte, len(b))
	copy(res, b)

	cur := 0
	for i, c := range b {
		k := idx[c] - 1
		if k >= 0 {
			for counts[cur] == 0 { cur++ }
			res[i] = vowels[cur]
			counts[cur]--
		}
	}
	return string(res)
}
