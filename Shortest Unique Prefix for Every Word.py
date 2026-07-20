class Solution:
    def findPrefixes(self, arr):
        # code here
        root = {"count": len(arr)}
        for word in arr:
            trie = root
            for c in word:
                if c in trie:
                    trie = trie[c]
                    trie["count"] += 1
                else:
                    trie[c] = trie = {"count": 1}
        answers = []
        for word in arr:
            trie = root
            for i in range(len(word)):
                trie = trie[word[i]]
                if trie["count"] == 1:
                    answers.append(word[:i + 1])
                    break
            else:
                answers.append(word)
        return answers
      
