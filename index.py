#DECORATORS-------------------------------------------------------------------------------------------

 
def fun_decorate(func):
 def wrapper():
  print("im rahul")
  func()
  print("Thank you")
  
 return wrapper

  
@fun_decorate
def printer():
  print("on the way...............")
printer()







# for i in range(3, 30):----------------------------------------------------------------------------------------------
#     if i % 3 == 0:
#        continue
#     print(i)
 
  
# for i in range(0, 21):
#     pass


# num=50
# value= 0
# if num <= 300:
#     if num<=100:
#         print(num-5)
#     if num <= 200:
#         print("0")
#     else:
#         value=10
#         print(num*value)
        

# else:
#         value = 20
#         print(num*value)
 
# #  class
# def fact(n):
#     if n == 1:
#       return 1
#     print(n)
#     return n * fact(n-1)
      
# res = fact(5)       
# print(res)
  



#arbidery arguments------------------------------------------------------------------------
# def sum(a,b,**c):

#   return a,b,c
# print(sum(2,3,d=8,e=14,f=23))
  

# a=10

# def num():
#    a=15
#    a=50
#    globals()['a'] = 25
#    print(a)
#    globals()['a'] = 30
# num()
  
# print(a)
   

# lamda function-----------------------------------------------------------------------------------
# lamb_fnnc = lambda x: x * x
# print(lamb_fnnc(10))
# print(lamb_fnnc(5))

 #map , filter, reduce----------------------------------------------------------------------------
# def sq(x):
#     return x * 2
# list1 = [1,2,3,4,5]
# print(list(map(sq,list1)))


# list1 = [1,2,3,4,5]
# print(list(map(lambda x: x* 2,list1)))


# list1 = [1,2,3,4,5]
# print(list(filter(lambda x: x%2==0,list1)))

# from functools import reduce
# list1 = [1,2,3,4,5]
# print(reduce(lambda x,y: x*y ,list1))

