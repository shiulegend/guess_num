# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 20:36:25 2023

@author: shiul
"""
#for i in range(1, 10):
 #   for j in range(1, 10):
  #      print("%d * %d = %d" % (i, j, i*j))
   # print()

import random

start = input ('請輸入數字開始值 : ')
end = input ('請輸入數字結整值 : ')
start = int (start)
end = int (end)

random_num = random.randint(start, end)
count = 0
while True :
    count += 1 
    pwd = input('請輸入猜的數字 : ')
    pwd = int (pwd)
    if pwd == random_num:
        print('你猜對了!')
        print('你猜了' , count , '次!')
        break
    elif pwd > random_num:
            print ('你猜的數字比答案大' )
    elif pwd < random_num :
            print ('你猜的數字比答案小')
    print('你猜了' , count , '次!')