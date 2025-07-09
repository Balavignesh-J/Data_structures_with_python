from template import user_template

class TrieNode:
    def __init__(self):
        self.children={}
        self.IsEnd=False

class Trie:
    def __init__(self):
        self.root=TrieNode()

    def add(self,word):
        current=self.root
        for char in word:
            if char not in current.children:
                current.children[char]=TrieNode()
            current=current.children[char]
        current.IsEnd=True

        print(f"{word} is Successfully inserted into the Trie")

    def search(self,word):
        current = self.root
        for char in word:
            if char not in current.children:
                return False
            current = current.children[char]

        if current.IsEnd:
            return True

    def remove(self,word):
        if not self.search(word):
            return False

        stack=[]
        current = self.root
        for char in word:
            stack.append(current)
            current = current.children[char]
        current.IsEnd = False

        while stack:
            node=stack.pop()
            char=word[len(stack)]
            child = node.children[char]
            if not child.IsEnd and not child.children:
                del node.children[char]
            else:
                break

        print(f"{word} is successfully deleted")



user_template(Trie)