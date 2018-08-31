Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> print"I love you"
SyntaxError: invalid syntax
>>> print'I love you'
SyntaxError: invalid syntax
>>> list1 = ['Hello', 'Python', 2018, 814]
>>> list1[0]
'Hello'
>>> print "list1[0]: "
SyntaxError: Missing parentheses in call to 'print'. Did you mean print("list1[0]: ")?
>>> print ("list1[0]: ")
list1[0]: 
>>> print('list1[0]')
list1[0]
>>> 
>>> print(list1[0])
Hello
>>> for i in range(1,11):
	print(i)
i = 1
while i < 6:
    i = i + 1
    print(i)
    
SyntaxError: invalid syntax
>>> i = 1
while i < 6:
    i = i + 1
    print(i)
    
SyntaxError: multiple statements found while compiling a single statement
>>> 
>>> for n in (1,10):
	print(n)
	
