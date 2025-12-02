class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        List = []
        word = 0

        for i in words[word]:
            found = True
            for j in range(word+1, len(words)):
                if i not in words[j]:
                    found = False
                    break
            if found:
                List.append(i)
                words = [w.replace(i, "",1) for w in words]
        return List
