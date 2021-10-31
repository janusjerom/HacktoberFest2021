# Problem Statement – An automobile company manufactures both a two wheeler (TW) and a four wheeler (FW). A company manager wants to make the production of both types of vehicle according to the given data below:

# 1st data, Total number of vehicle (two-wheeler + four-wheeler)=v
# 2nd data, Total number of wheels = W
 

# The task is to find how many two-wheelers as well as four-wheelers need to manufacture as per the given data.
# Example :

# Input :

# 200  -> Value of V
# 540   -> Value of W
# Output :

# TW =130 FW=70
v=int(input())
w=int(input())
if (w<2 or w%2!=0 or w<=v):
	print("INVALID INPUT")
else:
	x=((4*v)-w)//2
	print("TW={0} FW={1}".format(x,v-x))
