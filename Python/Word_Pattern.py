# https://leetcode.com/problems/word-pattern/description/
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        pattern_to_string_map = {}
        seen_charset = set()

        chars = s.split(" ")

        if len(pattern) != len(chars):
            return False

        for index, current_char in enumerate(chars):
            print(pattern_to_string_map)
            pattern_char = pattern[index]
            if pattern_char in pattern_to_string_map:
                print(f"checking if {pattern_char} maps to {current_char}")
                if pattern_to_string_map[pattern_char] != current_char:
                    return False
            else:
                print(f"mapping {pattern_char} to {current_char}")
                pattern_to_string_map[pattern_char] = current_char
                if current_char in seen_charset:
                    return False
                seen_charset.add(current_char)
        return True
