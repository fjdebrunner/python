#!/usr/bin/python

class Counter:
   total = 0
   testStart = 24
   testEnd = 53

   def __init__(self, num):
      self.num = num
      Counter.total = Counter.total + num;
      
   def reset(self, num=0):
      Counter.total = num

for i in range (Counter.testStart, Counter.testEnd):
  
   test = Counter(i)
   print (Counter.total)

   if i == Counter.testEnd - 1:
      test.reset()
      print (Counter.total)

