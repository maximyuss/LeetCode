class Solution {
public:
    bool isNStraightHand(vector<int>& hand, int groupSize) {
        struct Dict { int key; int val; };
        if (hand.size() % groupSize > 0) return false;
        vector <Dict> arr;
        sort(hand.begin(), hand.end());
        int val = hand[0], count = 1;
        for (size_t i = 1; i < hand.size(); i++) {
            if (hand[i] == val)
                count++;
            else {
                arr.push_back({ val,count });
                val = hand[i];
                count = 1;
            }
        }
        arr.push_back({ val,count });
        int n = arr.size();
        for (int i = 0; i < n; i++) {
            count = arr[i].val;
            if (count > 0) {
                if (i + groupSize > n or arr[i + groupSize - 1].key != arr[i].key + groupSize - 1)
                    return false;
                for (int j = i; j < i + groupSize; j++) {
                    if (arr[j].val < count)
                        return false;
                    arr[j].val -= count;
                }
            }
        }
        return true;
    }
};
