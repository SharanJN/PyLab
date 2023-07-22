# Aim: Demonstartion of manipulation of strings using string methods

# Write a python program to find the similarity between two given strings

str1 = input('Enter string 1 \n')
str2 = input('Enter string 2 \n')

if len(str2) < len(str1):
    short_one = len(str2)
    long_one = len(str1)
else:
    short_one = len(str1)
    long_one = len(str2)
    
matchCnt = 0

for i in range(short_one):
    if str1[i] == str2[i]:
        matchCnt += 1
    
print('Similarity between two said strings: ')
print(matchCnt/long_one)