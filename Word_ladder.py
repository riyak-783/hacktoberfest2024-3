from collections import deque

def word_ladder(beginWord, endWord, wordList):
    wordSet = set(wordList)
    if endWord not in wordSet:
        return 0
    
    queue = deque([(beginWord, 1)])
    while queue:
        current_word, steps = queue.popleft()
        if current_word == endWord:
            return steps

        # Try changing each character
        for i in range(len(current_word)):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                new_word = current_word[:i] + c + current_word[i+1:]
                if new_word in wordSet:
                    wordSet.remove(new_word)
                    queue.append((new_word, steps + 1))
    
    return 0

# Example usage
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
print(word_ladder(beginWord, endWord, wordList))  # Output: 5 ("hit" -> "hot" -> "dot" -> "dog" -> "cog")
