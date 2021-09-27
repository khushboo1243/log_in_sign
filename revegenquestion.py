# a=4+5*4/2
# print(a)

# a=["hello"]
# b=[]
# i=0
# while i<=len(a):


# num=int(input("enter the number: "))
# i=0
# a=[]
# while i<=10:
#     name=input("enter the name: ")
#     a.append(name)
#     i=i+1
# print(a)    

# i=0
# a=[]
# while i<=5:
#     a.append("hello")

#     i=i+1
# print(a)

# num=int(input("enter the rever number: "))
# i=0
# r=0
# c=0
# b=0
# a=0
# while i>0
# a=num%10
# b=r*a+10
# c=b//10
# print(c)   
# r=0
# a=0
# b=r*a+10
# print(b)
# print(b//10)

# num=int(input("enter the number"))
# cont=0
# while num>0:
#     count=count+num
#     a=count//10
# print(a)    




# n=int(input("Enter number:"))
# count=0
# while(n>0):
#    count=count+1
#    n=n//10
# print("The number of digits in the number is:",count)
# num=int(input("enter the number: "))
# count=0
# while num>0:
#     count=count+1
#     num=num//10
# print(count)    


# num=int(input("enter the number: "))
# i=0
# while i<=num:
#     print()
#     i=i+1

# num=int(input("enter the number: "))
# i=0
# r=0
# while (num>0):
#     b=num%10
#     r=r*10+num
#     num=num//10
# print(r)





# n=int(input("Enter number: "))



# rev=0
# while(n>0):
#    dig=n%10
#    rev=rev*10+dig
#    n=n//10
# print("The reverse of the number:",rev)  


# num=int(input("enter the number: "))
# i=0
# sum=0
# while (num>0):
#     d=num%10
#     sum=sum+d
#     num=num//10
# print(sum)    


# num=int(input("enter the perfect number: "))
# i=0
# sum=0
# while i<num:
#     if i%num==0:
#         sum=sum+i
#     i=i+1
# if(sum==num):
#     print("it is perfect number: ",sum)
# else:
#     print("it is not perfct number: ", sum)            

# n = int(input("Enter any number: "))
# sum1 = 0
# for i in range(1, n):
#    if(n % i == 0):
#       sum1 = sum1 + i
# if (sum1 == n):
#     print("The number is a Perfect number!")
# else:
#      print("The number is not a Perfect number!")


# string=raw_input("Enter string:")
# vowels=0
# for i in string:
# if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
# vowels=vowels+1
# print("Number of vowels are:")
# print(vowels)

# num=(input("enter the name"))
# i=0
# while i<=num:
#     if i=="k" or i=="h" nn
# 
# or i=="u" or i=="s" or i=="b" or i=="o"or i=="o":
#         i=i+1
#     print(i)



# list1=[1,2,3,4]
# i=0
# n=[]
# while i<len(list1):

# num=int(input("enter the number: "))
# i=0
# a=[]
# while i<=(num):
#     num1=input("enter the number: ")
#     a.append(num1)
#     i=i+1
# print(a)    


# num1=int(input("enter the number: "))
# num2=int(input("enter the number: "))
# num3=int(input("enter the number:"))
# i=0
# a=[]
# while i<=num1:
#     a.append(num1[i])
#     i=i+1
# print(a)
# d=[]
# i=0
# n=[]
# while i<=3:
#     num1=int(input("enter the number: "))
#     num2=int(input("enter the number: "))
#     num3=int(input("enter the number: "))
#     n.append(i[num1][num2][num3])
#     d.apppend[n]
# print(d)



# def findsubsets(s, n): 
#     return list(itertools.combinations(s, n)) 

#




# def num(s):
#     a=[[]]
#     for i in s:
#         for j in a:
#             a=a+[list(i)+[j]]
#         return(a)
# num([1,2,3,4])            

# num=[1,2,3]
# a=[[]]
# i=0
# while i<len(num):
#     j=0
#     while j<len(a):
#         a=a+list(i)+[j]
#     print(a)
#     j=j+1
# i=i+1    


# def powerset(x):
#     m=[]
#     if not x:
#         m.append(x)
#     else:
#         A = x[0]
#         B = x[1::]
#         for z in powerset(B):
#             m.append(z)
#             r = [A]+ z
#             m.append(r)
#     return(m)

# print(powerset([1, 2, 3, 4]))
# num=[1,2,3,4]
# m=[]
# if not num:
#     m.append(num)
# else:
#     a=num[0]
#     b=num[1:]
#     i=0
#     for i in num(b):
#         m.append(i)
#         r=[a]+i
#         m.append(r)
#         i=i+1
#     print(m)


# n = int(input())
# l = [i for i in range (1, n + 1)]

# for number in range(2 ** n) :
#     binary = bin(number)[: 1 : -1]
#     subset = [l[i] for i in range(len(binary)) if binary[i] == "1"]
#     print(set(sorted(subset)) if number > 0 else "{}")


# colours = [1,2]
# for i in colours:
#     if i == "red":
#         colours += ["black"]
#     if i == "black":
#         colours += ["white"]
# print(colours)




# def sub_lists (l):
#     lists = [[]]
#     for i in range(len(l)+1):
#         for j in range(i):
#             lists.append(l[j:i+1])
#     return lists
# l1 = [1, 2, 3]
# print(sub_lists(l1))

# animaldict = {
#   "name": "Dog",
#   "age":5,
#   "Weight": 4,
#   "Country": "US",
#   "City":"California"
   
# }
# dictlang = {'c#': 6, 'GO': 89, 'Python': 4,'Rust':10}
 
# for _ in (dictlang):
#     print (dictlang[_])


# name={"name":"khusboo","age":18,"subject":"hindi"}
# for i in sorted(name):
#     print(name[i]) 

# animaldict = {
#   "animal":{
#   "name": "Dog",
#   "age":5,
   
  
#   },
#     "animal1":{
#   "name": "Cat",
#   "age":2,
 
  
#   },
#     "animal2":{
#   "name": "Rabbit",
#   "age":1,
  
  
#   },
 
   
# }

# for i in animaldict:
#     print(animaldict)    



# b = "Hello, World!"
# print(b[2:]) 


# a="hello,word"
# print(a[2:5])

# num=[1,2,3,5,8]
# print(num[1:5])

num=["ram",10,"shyam",2.25,4,9,8,7]
# print(num[3:])
print(num[1::5])

