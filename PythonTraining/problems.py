# -*- coding: utf-8 -*-
"""
Created on Wed Feb 16 23:48:37 2022

@author: Albert
""" 

listOfWords = ["flower","flow","flight", "flw"]

def divide(word, howManyTimes):
    char = []
    if len(word) % 2 == 0:

        for i in range(0,howManyTimes+2,2):
            char.append(word[i] + word[i+1])
        return char
            
    else:
        for i in range(howManyTimes+1):
            char.append(word[i] + word[i+1])
        return char
    
def checkDupli(longList):
    for i in range(longList):
        print(longList[i])

def longestCommonPrefix(listOfWords):
        allCombinations = []
        for i in range(len(listOfWords)):
            howMany = len(listOfWords[i]) // 2
            a = divide(listOfWords[i], howMany)
            
            allCombinations.append(a)
            
        allDescCombinations = []
        for j in allCombinations:
            for z in j:
                allDescCombinations.append(z)
        
        duplicates = []
        print(allDescCombinations)
        check = ""
        for k in range(len(allDescCombinations)):
            if allDescCombinations[k] in check:
                continue
            else:
                for x in range(len(allDescCombinations) - allDescCombinations.index(allDescCombinations[k])+1):
                    print(allDescCombinations[x])
            print(k)
            check += allDescCombinations[k]
            
            
            
longestCommonPrefix(listOfWords)
























































'''
s = "MCMXCIV"

Generalsymbols = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}

ExceptionsGeneralSymbols = {
    "IV": 4,
    "IX": 9,
    "XL": 40,
    "XC": 90,
    "CD": 400,
    "CM": 900
}


def roman(s):

    symbol = ""
    usedSymbols = ""
    endSymbols = ""
    symbolsValue = 0
    
    # Problem z petla jest taki ze ostatni element z zmiennej s kiedy dodamy do niego jeden wyjdzie poza index i jest blad
    # napisac nowa pentle jesli s[i+1] nie jest undefined to wykonuj jesli jest to break
    
    for i in range(len(s)):
        try:
            symbol = s[i] + s[i+1]
            if symbol in ExceptionsGeneralSymbols:
                symbolsValue += ExceptionsGeneralSymbols[symbol]
                usedSymbols += symbol
        except IndexError:
            break
        
    #print(symbol)
    #print(exceptionsValue)
    #print(s ,usedSymbols)
    endSymbols = s.replace(usedSymbols, '')
    
    if len(endSymbols) <= 1:
        symbolsValue += Generalsymbols[endSymbols]
    else:
        for j in endSymbols:
            symbolsValue += Generalsymbols[j]
    #print(endSymbols)
    return symbolsValue
print(roman(s))
'''

'''
x = -121
myArr = []
another = []
compare = []

def isPalindrom(x):
    x = str(x)
    for i in range(len(x)):
        myArr.append(x[i])
        another.append(i)
        
    another.sort(reverse=True)
    
    for j in another:
        compare.append(myArr[j])
        
    if myArr == compare:
        return True
    else:
        return False
    
isPalindrom(x)
'''