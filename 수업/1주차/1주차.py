Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:57:54) [MSC v.1924 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 1/2
0.5
>>> 1//2
0
>>> 5/3
1.6666666666666667
>>> 5//3
1
>>> 7%4
3
>>> 7.8%3
1.7999999999999998
>>> 4%2.2
1.7999999999999998
>>> #나누기 ~ 나머지
>>> 3.141592*(3*3)
28.274328
>>> 3.141592*3**2
28.274328
>>> 3.141592*9**2
254.468952
>>> 3*4**3
192
>>> #**으로 제곱 표현가능
>>> pi= 3.141592
>>> pi= * 4**2
SyntaxError: can't use starred expression here
>>> pi*4**2
50.265472
>>> pi*2.5**2
19.63495
>>> printf(pi)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    printf(pi)
NameError: name 'printf' is not defined
>>> print(pi)
3.141592
>>> r=7
>>> area = pi*r**2
>>> print(area)
153.938008
>>> r=11
>>> area=pi*r**2
>>> print(area)
380.132632
>>> #변수사용1
>>> name1 ="Trump"
>>> name2 = '강다니엘'
>>> print(name1)
Trump
>>> print(name2)
강다니엘
>>> #변수사용2 ~ 변수에 문자열 담기
>>> type(order)
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    type(order)
NameError: name 'order' is not defined
>>> order =4
>>> type(order)
<class 'int'>
>>> type(pi)
<class 'float'>
>>> type(name)
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    type(name)
NameError: name 'name' is not defined
>>> type(name1)
<class 'str'>
>>> #자료형찾기
>>> 4>3
True
>>> 3.5<-1.3
False
>>> 1000==1000
True
>>> 99>=99
True
>>> a = 1>1
>>> print(a)
False
>>> type(a)
<class 'bool'>
>>> #비교연산
>>> first = "Seoung eun"
>>> last = "B"
>>> name = first+" " last
SyntaxError: invalid syntax
>>> name = first+" "+last
>>> name
'Seoung eun B'
>>> print(name)
Seoung eun B
>>> name*2
'Seoung eun BSeoung eun B'
>>> name*4
'Seoung eun BSeoung eun BSeoung eun BSeoung eun B'
>>> name[0]
'S'
>>> name[2]
'o'
>>> name[-2]
' '
>>> name[-1]
'B'
>>> #str
>>> title = "Python 2d Game Programming"
>>> title[0:6]
'Python'
>>> title[7:9]
'2d'
>>> title[:6]
'Python'
>>> title[-11:]
'Programming'
>>> title[::2]
'Pto dGm rgamn'
>>> title[::-1]
'gnimmargorP emaG d2 nohtyP'
>>> #Slice - [::] 문자열 일부 잘라냄
>>> twice =['momo','sana','zwi','nayun','dahyun']
>>> abc = ['a','b','c']
>>> twice
['momo', 'sana', 'zwi', 'nayun', 'dahyun']
>>> twice.append('jihyo')
>>> twice
['momo', 'sana', 'zwi', 'nayun', 'dahyun', 'jihyo']
>>> twice.sort()
>>> twice
['dahyun', 'jihyo', 'momo', 'nayun', 'sana', 'zwi']
>>> len(twice)
6
>>> unit = twice + abc
>>> unit
['dahyun', 'jihyo', 'momo', 'nayun', 'sana', 'zwi', 'a', 'b', 'c']
>>> unit.remove('momo')
>>> unit
['dahyun', 'jihyo', 'nayun', 'sana', 'zwi', 'a', 'b', 'c']
>>> unit[0]
'dahyun'
>>> unit[-1]
'c'
>>> unit[:3]
['dahyun', 'jihyo', 'nayun']
>>> #List(리스트) ~ (리스트도 슬라이스 적용가능)
>>> score = {'momo':80, 'zwi':85,'sana':98}
>>> type(score)
<class 'dict'>
>>> score['momo']
80
>>> score['nayun']=100
>>> score
{'momo': 80, 'zwi': 85, 'sana': 98, 'nayun': 100}
>>> del score['momo']
>>> score
{'zwi': 85, 'sana': 98, 'nayun': 100}
>>> score.keys()
dict_keys(['zwi', 'sana', 'nayun'])
>>> score.values()
dict_values([85, 98, 100])
>>> 'zwi' in score
True
>>> 'momo' in score
False
>>> score.clear()
>>> score
{}
>>> #Dictionary
>>> t1 =(1,2,3)
>>> t2=(1,)
>>> t3 =()
>>> t4 =1,2,3,4
>>> t4
(1, 2, 3, 4)
>>> type(t4)
<class 'tuple'>
>>> t5 =(1,'a',"park",(1,2))
>>> t1[1:]
(2, 3)
>>> t1+t5
(1, 2, 3, 1, 'a', 'park', (1, 2))
>>> t4*t4
Traceback (most recent call last):
  File "<pyshell#108>", line 1, in <module>
    t4*t4
TypeError: can't multiply sequence by non-int of type 'tuple'
>>> t4*2
(1, 2, 3, 4, 1, 2, 3, 4)
>>> #Tuple - 리스트와 유사, 값 바꿀 수X => 변경되지 않는 값들의 모임
>>> s1={1,2,3}
>>> type(s1)
<class 'set'>
>>> s1 = {1,2,2,4}
>>> s1
{1, 2, 4}
>>> l1={1,2,2,2,2,3,3,3,5,5,}
>>> s1 = set(l1)
>>> s1
{1, 2, 3, 5}
>>> s2 = {3,5,6,7}
>>> s1+s2
Traceback (most recent call last):
  File "<pyshell#120>", line 1, in <module>
    s1+s2
TypeError: unsupported operand type(s) for +: 'set' and 'set'
>>> s1|s2
{1, 2, 3, 5, 6, 7}
>>> s1&s2
{3, 5}
>>> s2-s1
{6, 7}
>>> s1-s2
{1, 2}
>>> s2.add(8)
>>> s1
{1, 2, 3, 5}
>>> s2.remove(6)
>>> s2
{3, 5, 7, 8}
>>> #set
>>> #중복허용X, 순서가 없음
>>> >>> import random
>>> random.randint(1,6)
3
>>> random.randint(1,6)
4
>>> random.randint(1,6)
5
>>> random.randint(1,6)
6
>>> random.randint(1,6)
3
>>> minus = input("Enter hour: ")
Enter hour: 4
>>> sec = minus*60
>>> sec
'444444444444444444444444444444444444444444444444444444444444'
#변수 타입 설정 -> 입력받았는데 str라서 이러한 결과가 나옴
>>> minus
'4'
>>> type(minus)
<class 'str'>
>>> m= int(minus)
>>> m
4
>>> type(m)
<class 'int'>
#변수 타입 설정2

