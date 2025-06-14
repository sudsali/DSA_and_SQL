class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        
        curr.word = word

    def search(self, word: str) -> bool:
        curr = self.root

        for c in word:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        
        return curr.endOfWord


    def startsWith(self, prefix: str) -> bool:

        curr = self.root

        for c in prefix:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        
        return True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()

        for word in words:
            trie.insert(word)

        root = trie.root

        res = set()

        rows,cols = len(board),len(board[0])

        def dfs(r,c,node):
            char = board[r][c]

            if char not in node.children:
                return
            
            next_node = node.children[char]

            if next_node.word:
                res.add(next_node.word)
            
            board[r][c] = '*'

            for dr,dc in [(0,1),(1,0),(-1,0),(0,-1)]:
                nr,nc = r+dr, c+dc
                if 0<=nr<rows and 0<=nc<cols and board[nr][nc]!= "*":
                    dfs(nr,nc,next_node)
            
            board[r][c] = char
        
        for i in range(rows):
            for j in range(cols):
                dfs(i,j,root)
        
        return list(res)
