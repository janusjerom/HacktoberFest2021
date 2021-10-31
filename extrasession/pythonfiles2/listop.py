lst = [int(x) for x in input()]
p=lst
a=[]
a+=lst

b=0
c=0
# print(a)
for i in range (len(lst)):
	b=(b*10)+max(p)
	p.remove(max(p))
	c=(c*10)+min(a)
	a.remove(min(a))
	
print(b,c)
