class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_t_map = {}
        t_s_map = {}

        for character in range(len(s)):
            current_s_char, current_t_char = s[character], t[character]
            if (current_s_char not in s_t_map) and (current_t_char not in t_s_map):
                s_t_map[current_s_char] = current_t_char
                t_s_map[current_t_char] = current_s_char
            elif s_t_map.get(current_s_char) != current_t_char or t_s_map.get(current_t_char) != current_s_char:
                return False

        return True
