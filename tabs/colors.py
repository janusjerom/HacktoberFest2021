import random

words = ['grey','black','red','pink','blue','peach','black','white']
val=random.choice(words)
x=int(len(val))
print(x)
z='_'
for i in range (1,6):
	for j in range (1,x+1):
		print (z,end=" ")
		print (end="_")
		word=input("Enter a character")
		if(word==val):
			print(word)
