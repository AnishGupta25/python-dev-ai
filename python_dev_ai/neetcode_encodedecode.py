class Solution:

    def encode(self, strs: List[str]) -> str:
        parts = []
        for word in strs:
            parts.append(f"{len(word)}/:{word}")
        return "".join(parts)

    def decode(self, s: str) -> List[str]:
        decoded_str = []
        i = 0
        while i < len(s):
            slash_idx = s.find("/:",i)
            length = int(s[i : slash_idx])
            i = slash_idx + 2
            decoded_str.append(s[i:i+length])
            i += length
        return decoded_str