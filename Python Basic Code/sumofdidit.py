# -*- coding: utf-8 -*-
"""
Created on Tue Mar  4 13:03:38 2014

@author: 3092
"""

n=int(input("enter a number"))
tot=0
while(n>0):
    dig=n%10
    tot=tot+dig
    n=n//10
    print("the total ",tot)