"""Develop a python program to convert binary to decimal, octal to hexadecimal using functions"""

def binaryToDecimal(binary):
    decimal, i = 0, 0
    while binary != 0:
        dec = binary % 10
        decimal = decimal + dec*pow(2,i)
        binary = binary//10
        i += 1
    print(decimal)
    return decimal

def octalToDecimal(octal):
    decimal2, i = 0, 0
    while octal != 0:
        oct2 = octal % 10
        decimal2 = decimal2 + oct2 * pow(8,i)
        octal = octal // 10
        i+=1
    print(decimal2)
    return decimal2

def decToHexa(n):
    hexaDeciNum, temp = " ", 0
    while n != 0:
        temp = n % 16
        if temp < 10:
            hexaDeciNum = str(temp) + hexaDeciNum
        else:
            hexaDeciNum = chr(temp + 87) + hexaDeciNum
        n = n // 16
    return hexaDeciNum

bin = int(input('Enter Binary Number:'))
bdecimal = binaryToDecimal(bin)
print('Decimal number is:',bdecimal)

octal = int(input('Enter Octal Number: '))
odecimal = octalToDecimal(octal)
print('Decimal number is: ',odecimal)

hex = decToHexa(odecimal)
print('Hexa-Decimal number for the given octal number is: ',hex)