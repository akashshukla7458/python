# print('hello')


# ******by default print ends with '/n' however we can change it

# print('hello', '4.5', end='|')


# **********naming convention in pyhton :  u can't use special char or start var name form number 
# _name is invalid only _ is exception for chars  you can name like hello_world 




# *****  AIRTHMETIC OPERATORS******

# x=10
# y=3

 # floor division
# res= x//y 

# res= x/y   #by default ans will be in float type
# res= x**y   #exp operator
# print(res)




# *******by defualt python takes input as string

# num= input('Number: ')
# print(int(num)-5)




# **************  list are mutable change to list apllies to other also it doesnt copy but refers same

# x= [4,'hi', True];
# y= x;
# x[0]= 'hello';
# print(x,y)



# x= [4,'hi', True];
# y= x[:];
# x[0]= 'hello';
# print(x,y)

# for i in range(1, 10,1):
#     print(i)

# start stop end


# *************list

# x=[0,1,2,3,4,5,6,7,8];

# sliced=x[::-1]  reverse list

# sliced= x[start:end:step]
# print(sliced)

# set in python sets are faster than list

# s={4,32, 5, 4}
# print(type(s))
# print (4 in s)


#**********  dictionary is same as hashmap
# x={'key': 4}
# x['2']=8
# print(x)

# for key in x:
#     print(key, x[key] )


#******comprehensions

# x= tuple(i for i in range(10) if i%5==0)
# print(x)


# *******args kwargs

# def func(*args, **kwargs):
#     pass

# x=[1,23, 3455, 5667]
# print(*x)  # sepeartes all element , unpacking
# ** for dictionaries and * for list ans tuples




# def func(x,y):
#     print(x,y)
    
# func(**{'y':5, 'x':2})


# *****lambda function

# x= lambda x: x+5
# print(x(2))

#********* map function

# x= [1,2,3,4,5,6,7]
# mp= map(lambda i:i+2,x)
# print(list(mp))


# ********filter function

# mp= filter(lambda i: i%2==0, x)
# print(list(mp))
