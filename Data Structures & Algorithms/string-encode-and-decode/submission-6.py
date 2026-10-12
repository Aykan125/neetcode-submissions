class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs==[]:
            return "nostring"
        return ".".join(strs)
    def decode(self, s: str) -> List[str]:
        if s == "nostring":
            return []
        return s.split(".")

