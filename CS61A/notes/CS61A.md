print function returns None
|This expression  | Evaluates to  |Interactive Output
|---|---|---|
5|5|5
print(5)|None|5
print(print(5))|None|5 //None
 delay(delay)()(6)()|6|delayed//delayed//6
```Python
def delay(arg):
    print('delayed')
    def g():
        return arg
    return g
delay(delay)()(6)()
def pirate(arggg):
    print("matey")
    def plunder(arggg):
        return arggg
    return plunder
```
**查找名称的过程总是在当前环境的第一个框架上进行
The process for looking up a name always looks on the first frame of the current environment.**
```python
def horse(mask):
    horse =mask
```
# recursion
```python
def print_all
    print(x)
    return print_all
>>>print(1)(3)(5)
    1 
    3
    5
```
## Recursive Functions
Def : A function is called recursive if the body f that function calls itself, either directly or indirectly.
Implication: Executing the body of a recursive function may require applying that function again.
### sum digits without a while statement
```python
def split(n):
    return n//10,n%10
def sum_digits(n):
    if n<10:
        return n
    else:
        all_but_last,last= split(n)
        return sum_digits(all_but_last) +last #recursive calls

```
通常以一个base case 开始 属于没有递归的情况
**recursive cases are evaluated with recursive calls**


## Recursion in environment diagrams 
**在递归中 直到base case的情形触发 从base case所在的帧开始返回**
![alt text](image-11.png)
- The same function "fact" is called multiple times
- different frames keep track of the different arguments in each call
- what n evaluates to depends upon which is the current environment
- each call to fact solves a simpler problem than the last : simpler n

### Iteration vs Recursion




### The Recursive Leap of Faith

Is fact implemented correctly?
1. verify the base case
2. Treat fact as a functional abstraction!
3. Assume that fact(n-1) is correct
4. verify that fact(n) is correct, assuming that fact(n-1) correct.
***这不数学归纳法吗***
## Mutual recursion

### The Luhn Algorithm
'


# Tree recursion

## order of recursive calls
 ```python
 def cascade(n):
    if n<10:
        print(n)
    else:
        print(n)
        cascade(n//10)
        print(n)
>>> cascade(123)
123
12
1
12
123
```
![alt text](image-13.png)
**Until return value appears, that call has not completed.**

### Inverse Cascade




Fibonacci number
```python
def fib(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fib(n-1)+fib(n-2)

```
这不是很有效 很多数被重复计算了
Example: Counting partitions


# Lists
 
 ## Working with lists
 ### concatenation adn repetition
 ```python
 digits=[1,2,3,4]
 >>>[2,7]+digits*2
 [2,7,1,2,3,4,1,2,3,4]
 # Nested lists
 Pairs=[[10,20],[20,40]]
 >>> Pairs[1]
 [20,40]
 >>> Pairs[1][0]
 20
 ```
## Containers
```python
digits=[1,8,2,8]
>>> 1 in digits
True
>>> 5 in digits
False
>>>'1' in digits
False
>>> [1,8] in digits
False
```
## For statement
用for 语句直接索引整个列表
### sequence unpacking in for statement
**do sequence unpacking right inside the header of the statement**
```python
pairs=[[1,2],[2,2],[3,4][4,4]]
same_count=0
for x,y in pairs:
    if x==y :
        same_count +=1
x，y被绑定至大列表中的小列表里
```
## range
想象一条无限长的数轴线
range(x,y)对应了两个数之前 之间的范围**即左闭右开**
Length： ending value- starting value
Element selection : Starting value + index(*start from 0*)
```python
>>> list(range(4))# 注意是括号
[0,1,2,3]
```
## List Comprehensions
可以理解为对列表本身进行一种遍历的变换
还可以加限制条件
```python
odd=[1,3,5,7,9]
>>>[x+1 for x in odds]
[2,4,6,8,10]
>>> [x for x in odds if 25 % x == 0]
[1,5]
def devisor(n): # 一个可以计算n的因数的函数
    return [1]+ [x for x in range (2,n) if n%x == 0]
```
# Containers
## The Closure property of DAta types
- 如果这个数据类型满足封闭性质，那么这个组合结果本身可以使用相同的方法再次组合
-  封闭性（closure）是很有用的，允许我们创建分层结构
-  分层结构顾名思义
## Box- and - pointer notation in Environment diagrams

## SLicing

## Processing COntainer Values

### sequence aggregation
Several build- in function that take iterable arguments and aggregate them into a value
max 
all
sum

### Strings are an Abstraction
因为我们不关心他们是如何编码的，但他们的确代表信息

### String literals have three forms
'I am string'
"I've got an apostrophe"
"""The zen of Python 
claims, Readability counts.
Read more : import this.""" **三引号可以跨行**
转义符： 'the zen of python**\n**claims, '
### Strings are sequences
```python
>>>city = 'Berkeley'
>>> len(city)
8
However,the"in" and "not in" operators match substrings
>>> 'here' in " Where's Waldo"
True
>>> 234 in [1,2,3,4,5]
False
>>> [2,3,4] in [1,2,3,4,5]
False
```
# Dictionaries
Python中的字典是一种内置数据类型，用于存储键值对（pairs of a key）,键（key）用于查找某个值，对应的值即为你想要查找的内容
Dictionary is also sequences
```python
numerals={'x':1,'V':10,'I' : 5}
>>>list(numerals)


# 字典的值可以是列表，数字，字典
# 键之间不能相等
# 键本身不能是列表或者字典

```
## Dictionary Comprehensions

![alt text](image-20.png)
# Data abstraction




# representing rational numbers

## using list 
```python
pair=[1,2]
# list literal 列表字面量(x,y) comma-separated expression in brackets
>>> x,y=pair #unpacking
>>> x
1
>>> y
2
pair[0] #element selection operator from getitem
>>> getietm(pair,0)
1
def rational(n,d):
    """Construct a rational number that represents N/D"""
    return [n,d]
def numer(x):
    return x[0]
def nomin(x):
    return x[1]

```
## reducing to Lowest terms(约分)
如果按上面的形式运行 就会出现没有约分的数 实际上是对有理数本身的定义出了问题 
```python
from fraction import gcd (最大公约数)
def rational(n,d):
    g=gcd(n,d)
    return [n//g,d//g]

```
# Abstraction barriers（高重要性）
什么意思呢？ 其实是代码规范 就是说上层只通过接口(函数)来调用下层，对下层的内容原理一无所知。
好处是你需要修改代码是只需要改一层



# Tree abstraction








# objects
- objects represents information
- objects consist of data and behavior, bundle together to create abstraction
- A type of object is called a class. classes are first-class value in python
    - first-class value: 被当作‘普通值’对待的数据类型 可以做到：
        - 能复制给变量
        - 能当参数传进函数
        - 能作为返回值返回
        - 能放进数据结构里
object-oriented programming:
- A metaphor for organizing large programs
- special syntax that can improve the composition(结构) of our programs 
In python, every value is a object
Function only does one thing. Objects do many related things(methods).

## Sameness and change 

### is and ==
a is b means that a and b are bind to the same object(比较的是identity，对象身份)
a == b means that a and b have the same content.（比较的是value）

## Mutable default arguments are dangerous
 
## Mutable functions
```python
def make_withdraw_list(balance):
    b=list(balance)
    def withdraw(money):
        if b[0]< money:
            return  'insufficient balance'
        else :
            b[0]=b[0]-money
            return b[0]
    return withdraw
```
# Object-oriented programming
- A class defines how objects of a particular type behave
- An object is an instance of a class.The class is its type.
- A method is a function called on an object using a dot expression
```python   
# 创建一个银行账户类 有存钱取钱 户主余额等等
a= account('John')
>>> a.holder
'John'
>>> a.balance
0
# balance and holder are attributes
```
![alt text](image-22.png)
## Instance attributes
- The value of an existing attribute can be changed 
- A new attribute can be added at any time

## Invoking methods
dot notation automatically supplies the first argument(self) to a method
这样做是为了让特定的方法对应特定的类


# Attribute
## looking up Attributes by name
- First,evaluated the left of the dot, yields the object
- name is matched against the **instance attributes** of that objects 
- If not,<name> is looked up in the class, which yields a class attribute value.
- that value is returned unless it is a function, in which case a bound method(就是自带self的方法) is returned instead.

## Accessing attributes
- getattr and dot expression look up name in the same way

##  Assignment to attributes
- if the object is an instance, then sets an instance attribute
- if the object is a class,then sets a class attribute
- 对单个instance 赋值 的优先级高于 对class attribute的重新赋值[attribute  是列表除外]
## bound methods
A method is a class attributes and also a function

A bound method is a function that has its first parameter 'self' already bound to an instance
Dot expressions evaluates to bound methods for class attributes that are functions

# Inheritance 
- Inheritance is a method for relating classes together
- A common use : Two similar classes differ in their degree of specialization
- The specialized class may have the same attribute as the general class
    -  conceptually, the new subclass shares some attributes with its base class
    -  Also, the subclass may override some inherited attributes
- Using inheritance, we implement a subclass by specifying its difference from the base class
## Looking up attribute names on classes
**Base class attributes aren't copied into subclasses!**
*To look up a name in class*
 先在本类里面找，没有再进基类

# OOP Design

## Inheritance and composition
we usually take class as a real world thing in oop
- Inheritance is best for representing  **is-a** relationship
  - E.g., a checking account is a specific type of account
- Composition is best for representing **has-a** relationship
  - E.g., a bank has a collection of bank accounts it manages
## Attributed lookup practice
         








