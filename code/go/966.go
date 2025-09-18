// https://leetcode.com/problems/vowel-spellchecker/
func spellchecker(wordlist []string, queries []string) []string {
	dict0 := make(map[string]struct{})
	dict1 := make(map[string]string)
	dict2 := make(map[string]string)

	normalize := func(s string) string {
		return strings.Map(func(r rune) rune {
			switch r {
			case 'a', 'e', 'i', 'o', 'u':
				return '*'
			default:
				return r
			}
		}, s)
	}

	for _, word := range wordlist {
		dict0[word] = struct{}{}
		val1 := strings.ToLower(word)
		if _, ok := dict1[val1]; !ok { dict1[val1] = word }
		val2 := normalize(val1)
		if _, ok := dict2[val2]; !ok { dict2[val2] = word }
	}

	res := make([]string, len(queries))
	for i, query := range queries {
		if _, ok := dict0[query]; ok {
			res[i] = query
			continue
		}
		val1 := strings.ToLower(query)
		if v, ok := dict1[val1]; ok {
			res[i] = v
			continue
		}
		val2 := normalize(val1)
		if v, ok := dict2[val2]; ok {
			res[i] = v
		} else {
			res[i] = ""
		}
	}
	return res
}
