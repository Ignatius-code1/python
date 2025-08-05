# your function only takes 3 parameters
#your function 4 or 5 or 6 parameters
#args > argumemts


def greet (person1, person2, person3,):
   print (person1)
   print (person2)
   print (person3)


def greet (*args):
   for arg in args:
      print ("Name is", arg)
greet ("Sam","Alice","Bob","Charlie")


def sum(*args):
   ans = 0
   for n in args:
      ans += n
   print("Ans is ", ans)
   return ans
sum(100,20,30,40,50,60,70,80,90,100)

