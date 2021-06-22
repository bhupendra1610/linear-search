def linear_search(s,n):
   list2=[]
   flag=False
   
   for i in range(0 ,len(s)):
       if n==s[i]:
           flag =True
           list2.append(i)

   if flag==True:
       for i in list2:
           print(i)
   else:
       print('ele not found')
   return i
   
   
s=input().split()   # list input
n=input()    # number to be searched 
linear_search(s,n)   # call function
