class Solution:
    def reverseWords(self, s: str) -> str:
        s_list = list(s.split())
        
        result = []
        for word in s_list:
            w_list = list(word)
            w_list.reverse()
            word = "".join(w_list)
            result.append(word)
        
        return " ".join(result)