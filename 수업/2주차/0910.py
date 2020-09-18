a = 'AAA'
b = 'BBB'
a,b = b,a
a
b
a,b,c = 'a','b','c'
a,b,c = b,c,a
print(a,b,c)
for n in [1,3,4,5]:
	print(n)
for c in "Lee DAE HYUN":
	print(c)
sum = 0
for i in range(1,100+1):
	sum = sum+i
sum
def add(a,b):
	sum = a+b
	return sum
result = add(100,10)
print(result)
for i in range(10):
	print(i)
for i in range(10,20):
	print(i)
for i in range(1,10+1):
	print(i)
import turtle
pos = turtle.pos()
x,y = pos
pos = 123,45
x,y = pos
x
y
pos
turtle.goto(pos)
