// https://leetcode.com/problems/compare-version-numbers/
func compareVersion(version1 string, version2 string) int {
    parts1 := strings.Split(version1, ".")
    parts2 := strings.Split(version2, ".")
    
    maxLen := len(parts1)
    if len(parts2) > maxLen { maxLen = len(parts2) }

    for i := 0; i < maxLen; i++ {
        var v1, v2 int        
        if i < len(parts1) { v1, _ = strconv.Atoi(parts1[i]) }
        if i < len(parts2) { v2, _ = strconv.Atoi(parts2[i]) }
        
        if v1 < v2 {
            return -1
        } else if v1 > v2 {
            return 1
        }
    }
    return 0
}
