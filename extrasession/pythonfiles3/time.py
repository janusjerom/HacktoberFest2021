#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
	if s[8]=='P':
		arr=list(s.split(":"))
		a=int(arr[0])
		a+=12
		if a==24:
			return("12:{0}:{1}{2}".format(arr[1],arr[2][0],arr[2][1]))
		else:
			return("{0}:{1}:{2}{3}".format(a,arr[1],arr[2][0],arr[2][1]))
	elif s[0]=='1' and s[1]=='2':
		arr=list(s.split(":"))
		return("00:{0}:{1}{2}".format(arr[1],arr[2][0],arr[2][1]))
	else:
		s.strip("AM")
		return(s)

if __name__ == '__main__':


	s = input()

	result = timeConversion(s)
	print(result)
