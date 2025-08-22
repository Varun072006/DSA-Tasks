class Solution:
    # Integer Input & Output
    def printInteger(self):
        num = int(input())
        print(num)
    
    # Float Input & Output
    def printFloat(self):
        num = float(input())
        print(num)
    
    # String Input & Output
    def printString(self):
        s = input()
        print(s)
    
    # Character Input & Output
    def printChar(self):
        ch = input()
        print(ch)

    # Boolean Input & Output
    def printBoolean(self):
        b = input()
        if b == 'True':
            print(True)
        elif b == 'False':
            print(False)

sol = Solution()