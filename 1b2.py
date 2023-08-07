n = input('Enter string:')

if(n[0::] == n[::-1]):
    print('The given string',n,'is a palindrome')
else:
    print('The given string',n,'is not a palindrome\n')
    
num = str(n)
for i in range(10):
    print('Number of occurances of',i,'in',n,'is',n.count(str(i)))