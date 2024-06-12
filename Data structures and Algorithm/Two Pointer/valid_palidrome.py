input_string = "RACEACAR"

class Palindrome:
    def __init__(self, s):
        self.s = s
    
    def check(self):
        s = self.s
        rev_s = self.s[:-1]
        print(rev_s)
        for i in range(int(len(self.s)/2)):
            print(i)
            if s[i] != rev_s[i]:
                return False
        return True
    
palindrome = Palindrome(input_string)
print(palindrome.check())

