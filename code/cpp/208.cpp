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
			if (node->next.count(c) == 0)
				node->next[c] = new TrieNode();
			node = node->next[c];
		}
		node->isEnd = true;
	}

	bool search(string word) {
		TrieNode* node = root;
		for (auto c : word) {
			if (node->next.count(c) == 0) 
				return false;
			node = node->next[c];
		}
		return node->isEnd;
	}

	bool startsWith(string prefix) {
		TrieNode* node = root;
		for (auto c : prefix) {
			if (node->next.count(c) == 0) 
				return false;
			node = node->next[c];
		}
		return true;
	}
};

/**
 * Your Trie object will be instantiated and called as such:
 * Trie* obj = new Trie();
 * obj->insert(word);
 * bool param_2 = obj->search(word);
 * bool param_3 = obj->startsWith(prefix);
 */
