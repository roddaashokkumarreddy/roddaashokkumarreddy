class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfString = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insertString(self, word):
        current = self.root
        for i in word:
            ch = i
            node = current.children.get(ch)
            if node == None:
                node = TrieNode()
                current.children.update({ch:node})
            current = node
        current.endOfString = True
        print("Successfully inserted")
    
    def searchString(self, word):
        currentNode = self.root
        for i in word:
            node = currentNode.children.get(i)
            if node == None:
                return "The word is not there"
            currentNode = node

        if currentNode.endOfString == True:
            return "The word is there"
        else:
            return "The Word is not there"
        

def deleteString(root, word, index):
    ch = word[index]
    currentNode = root.children.get(ch)
    canThisNodeBeDeleted = False

    if len(currentNode.children) > 1:
        deleteString(currentNode, word, index+1)
        return False
    
    if index == len(word) - 1:
        if len(currentNode.children) >= 1:
            currentNode.endOfString = False
            return False
        else:
            root.children.pop(ch)
            return True
    
    if currentNode.endOfString == True:
        deleteString(currentNode, word, index+1)
        return False

    canThisNodeBeDeleted = deleteString(currentNode, word, index+1)
    if canThisNodeBeDeleted == True:
        root.children.pop(ch)
        return True
    else:
        return False

    
newTrie = Trie()
newTrie.insertString("App")
newTrie.insertString("App1")
newTrie.insertString("App2")
newTrie.insertString("App3")
newTrie.insertString("App4")
deleteString(newTrie.root, "App2", 0)
deleteString(newTrie.root,"App4",0)
print(newTrie.searchString("App4"))
print(newTrie.searchString("App3"))
print(newTrie.searchString("App2"))
