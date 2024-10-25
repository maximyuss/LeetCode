//https://leetcode.com/problems/remove-sub-folders-from-the-filesystem/
class Solution {
public:
    vector<string> removeSubfolders(vector<string>& folder) {
        vector<string> res;
        sort(folder.begin(), folder.end());
        int l = 0;
        string s = folder[l] + "/";
        res.push_back(folder[l]);
        for (size_t i = 1; i < folder.size(); i++) {
            if (folder[i].starts_with(s))
                continue;
            l = i;
            s = folder[l] + "/";
            res.push_back(folder[l]);
        }
        return res;
    }
};
