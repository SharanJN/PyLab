"""Develop a Python program to check whether a given number is palindrome or not and also count the number of occurrences of each digit in the input number."""

n = int(input('Enter number/string to check if palindrome or not: '))

original = n
reverse = 0
while n!= 0:
    remainder = n%10
    reverse = reverse*10+remainder
    n = n//10
if original == reverse:
    print('The given number is ',original,'is palindrome')
else:
    print('The given number is',original,'is not palindrome')   
    
num = str(original)
for i in range(10):
    print('Number of occurances of',i,'in',num,num.count(str(i)))