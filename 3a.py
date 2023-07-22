# Aim: Demonstartion of manipulation of strings using string methods

#Write a python program that accepts a sentence and find the number of words, digits, uppercase letters and lowercase letters.

sentence = input('Enter a sentence:')

WordList = sentence.split(' ')

print('This sentence has',len(WordList),'words')

digCnt = upCnt = loCnt = 0

for ch in sentence: 
    if '0' <= ch <='9':
        digCnt += 1
    elif 'A' <= ch <= 'Z':
        upCnt += 1
    elif 'a' <= ch <= 'z':
        loCnt += 1


print('This sentence has ',digCnt,'digits', upCnt,"uppercase letters",loCnt,"lowercase letters")