""" Write a python program to find the best of two test average marks out of three test’s marks accepted from the user. """

m1 = int(input('Enter marks of test 1: '))
m2 = int(input('Enter marks of test 2: '))
m3 = int(input('Enter marks of test 3: '))

minimum = min(m1,m2,m3)
sum_of_2 = m1+ m2 + m3 -minimum
average = sum_of_2/2
print('Average of best of three tests is ',average)