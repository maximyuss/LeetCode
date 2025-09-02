class Solution {
    public int numberOfPairs(int[][] points) {
        Arrays.sort(points, (a, b) -> a[0] != b[0] ? Integer.compare(a[0], b[0]) : Integer.compare(b[1], a[1]));
        int res = 0;
        for (int i = 0; i != points.length - 1; i++) {
            int y0 = points[i][1], y_lower = -1;
            for (int j = i + 1; j != points.length; j++) {
                int y = points[j][1];
                if (y_lower < y && y <= y0) {
                    res++;
                    y_lower = y;
                }
                if (y0 == y_lower)
                    break;
            }
        }
        return res;
    }
}
