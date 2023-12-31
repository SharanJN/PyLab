"""Write a python program to find whether the given input is palindrome or not (for both 
string and integer) using the concept of polymorphism and inheritance."""

class PaliStr:
    def __init__(self):
        self.isPali = False 
    def chkPalindrome(self, myStr):
        if myStr == myStr[::-1]:
            self.isPali = True
        else:
            self.isPali = False 
        return self.isPali
 
class PaliInt(PaliStr):
    def __init__(self):
        self.isPali = False 
    def chkPalindrome(self, val):
        temp = val
        rev = 0
        while temp != 0:
            dig = temp % 10
            rev = (rev*10) + dig
            temp = temp //10
        if val == rev:
            self.isPali = True
        else:
            self.isPali = False
        return self.isPali
    
st = input("Enter a string : ")
stObj = PaliStr()
if stObj.chkPalindrome(st):
    print("Given string is a Palindrome")
else:
    print("Given string is not a Palindrome")
    
val = int(input("Enter a integer : ")) 
intObj = PaliInt()
if intObj.chkPalindrome(val):
    print("Given integer is a Palindrome")
else:
    print("Given integer is not a Palindrome")

"""

OUPUT: 

Enter a string: abcdedcba
Given string is a Palindrome. 
Enter an integer: 129
Given integer is not a Palindrome. 

Enter a string : qweq
Given string is not a Palindrome
Enter a integer : 12321
Given integer is a Palindrome
"""