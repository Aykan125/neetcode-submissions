class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs == []:
            return "ayman"
        return ".".join(strs)
    def decode(self, s: str) -> List[str]:
        if s == "ayman":
            return []
        return s.split(".")

