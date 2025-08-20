//https://leetcode.com/problems/find-consecutive-integers-from-a-data-stream/
class DataStream {
    private int val, k, cnt = 0;

    public DataStream(int value, int k) {
        this.val = value;
        this.k = k;
    }

    public boolean consec(int num) {
        if (num == val)
            cnt++;
        else
            cnt = 0;
        return cnt >= k;
    }
}
