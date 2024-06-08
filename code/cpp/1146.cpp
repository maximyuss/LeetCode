//https://leetcode.com/problems/snapshot-array/
class SnapshotArray {
private:
    struct Value {
        int index;
        int val;
    };
    unordered_map<int, vector<Value>> mp;
    int count = 0;
public:
    static bool comp(const int a, const Value& b) { return (a < b.index); }
    SnapshotArray(int length) {}
    void set(int index, int val) { mp[index].push_back({ count, val }); }
    int snap() { count++; return count - 1; }
    int get(int index, int snap_id) {
        const vector<Value>& curr = mp[index];
        auto it = upper_bound(curr.begin(), curr.end(), snap_id, comp);
        if (it == curr.begin())
            return 0;
        it--;
        return it->val;
    }
};

/**
 * Your SnapshotArray object will be instantiated and called as such:
 * SnapshotArray* obj = new SnapshotArray(length);
 * obj->set(index,val);
 * int param_2 = obj->snap();
 * int param_3 = obj->get(index,snap_id);
 */
