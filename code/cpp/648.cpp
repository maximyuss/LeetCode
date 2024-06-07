class Solution {
public:
    struct TrieNode {
        map<char, TrieNode*> next;
        bool isEnd = false;
    };

    class Trie {
        TrieNode* root;
    public:
        Trie() { root = new TrieNode(); }

        void insert(string word) {
            TrieNode* node = root;
            for (auto c : word) {
                if (node->isEnd) return;
                if (node->next.count(c) == 0)
                    node->next[c] = new TrieNode();
                node = node->next[c];
            }
            node->isEnd = true;
        }

        string replace(string word) {
            TrieNode* node = root;
            for (size_t i = 0; i < word.size(); i++) {
                if (node->isEnd)
                    return word.substr(0, i);
                if (node->next.count(word[i]) == 0)
                    return word;
                node = node->next[word[i]];
            }
            return word;
        }
    };

    #include <sstream>
    string replaceWords(vector<string>& dictionary, string sentence) {
        Trie dict;
        for (string word : dictionary) {
            dict.insert(word);
        }
        istringstream ss(sentence);
        string word, res;
        while (ss >> word) {
            res += dict.replace(word) + " ";
        }
        res.pop_back();
        return res;
    }
};
