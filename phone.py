#!/usr/bin/python
import sys
class Solution(object):
    def __init__(self):
        self.keyMap = {
                      '1':"",
                      '2':"abc",
                      '3':"def",
                      '4':"ghi",
                      '5':"jkl",
                      '6':"mno",
                      '7':"pqrs",
                      '8':"tuv",
                      '9':"wxyz",
                      '0':""
                      }
    def letterCombinations(self, digits):
        stringList = []
        self.dive(0,digits,stringList, "")
        return stringList

    def dive(self, pos, digits, stringList,currentStr):
        for char in self.keyMap[digits[pos]]:
            newString = currentStr + char
            if pos == len(digits)-1:
                stringList.append(newString)
            else:
                self.dive(pos+1,digits,stringList,newString)
        if pos == len(digits)-1:
            return stringList  

         
solution = Solution()
print solution.letterCombinations("23")
