## 2020/10/27

class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        self.nodes = preorder.split(',')
        return self.isValid() and len(self.nodes) == 0

    def isValid(self):
        if len(self.nodes) == 0: return False
        val = self.nodes.pop(0)
        if val == '#': return True
        left = self.isValid()
        right = self.isValid()
        return left and right

if __name__ == "__main__":
    print(Solution().isValidSerialization("9,3,4,#,#,1,#,#,2,#,6,#,#"))
    print(Solution().isValidSerialization("1,#"))
    print(Solution().isValidSerialization("9,#,#,1"))