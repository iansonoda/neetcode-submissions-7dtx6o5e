class TrieNode:
    def __init__(self):
        self.isWord = False
        self.children = {}

    def addWord(self, word: str):
        curr = self

        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()

            curr = curr.children[char]

        curr.isWord = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        res, visited = set(), set()
        root = TrieNode()

        for word in words:
            root.addWord(word)

        ROWS, COLS = len(board), len(board[0])

        def dfs(r, c, node, word):
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or
                (r, c) in visited or
                board[r][c] not in node.children):

                return


            # letter in the Trie, look at all 4 dirs

            visited.add((r, c))
            node = node.children[board[r][c]]
            word += board[r][c]

            if node.isWord:
                res.add(word)

            dfs(r + 1, c, node, word)
            dfs(r - 1, c, node, word)
            dfs(r, c + 1, node, word)
            dfs(r, c - 1, node, word)

            visited.remove((r, c))

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root, "")


        return list(res)

