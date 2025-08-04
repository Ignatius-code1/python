to_loop=True
i=0
while to_loop:
   print("i is", i)  # This will print indefinitely
   i=i+1
   if i>10:
      to_loop=False

k=0 
while k<10:
   print ("k is", k)  # This will print numbers from 0 to 9
   k=k+1


   for i in range(10):
      print("i is", i)  # This will print numbers from 0 to 9