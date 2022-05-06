#!/usr/bin/env python
# coding: utf-8

# In[6]:


# 1.Write a program to find all pairs of an integer array whose sum is equal to a given number
def pairCount(arr,summ):
    c=0
    for i in range(0,len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]+arr[j]==summ:
                c+=1
                print(arr[i],arr[j])
                 
            
    return c
arr=map(int ,input().split())
arr=list(arr)
summ=int(input("enter the number"))
count=pairCount(arr,summ)
print("Pairs in array present :",count)


# In[5]:


#2.Write a program to reverse an array in place? In place means you cannot create a new array.

def reverse(arr,l):
    t=0
    for i in range(len(arr)-1):
        if i<=l:
            t=arr[i]
            arr[i]=arr[l]
            arr[l]=t
            l-=1
        else:
            break
    return arr
    
arr=map(int ,input().split())
arr=list(arr)
length=len(arr)-1
rev=reverse(arr,length)
print(rev)


# In[ ]:


#3. Write a program to check if two strings are a rotation of each other
class Stack:
    def __init__(self,limit):
        self.limit = limit
        self.elements = []
        
    def push(self,number):
        if len(self.elements)== self.limit:
            print('stack is full')
        else:
            self.elements.append(number)
            
    def pop(self):
        if len(self.elements)==0:
            print('The stack is empty')
        else:
            #print(f'removing {self.elements[-1]} from the stack')
            return self.elements.pop()
            
    def peek(self):
        if len(self.elements)==0:
            print('The stack is empty')
        else:
            return self.elements[-1]
    
    def isEmpty(self):
        if len(self.elements)== 0:
            return True
        else:
            return False
        
    def isFull(self):
        if len(self.elements)==self.limit:
            return True
        else:
            return False
        
    def delete(self):
        self.elements=[]
        
    def print_stack(self):
        print('\n---------------- Current stack values ------------------\n')
        for item in self.elements:
            print(item,end=' ')
            
            
            
str1=input("Enter the first string :")
str2=input("Enter the second string :")
str2=list(str2)
ch=[]
stack1=Stack(len(str2))
for i in str2:
    stack1.push(i)
while not stack1.isEmpty():
    ch.append(stack1.pop())
str2="".join(ch)
if str1==str2:
    print("two strings are in rotation of each other")
else:
    print("two strings are NOT IN rotation of each other")
    
        
            
            


# In[ ]:


#4.Python program to print the first non-repeating character
NO_OF_CHARS = 256
 
# Returns an array of size 256 containing count
# of characters in the passed char array
def getCharCountArray(string):
    count = [0] * NO_OF_CHARS
    for i in string:
        count[ord(i)]+= 1
    return count
 
# The function returns index of first non-repeating
# character in a string. If all characters are repeating
# then returns -1
def firstNonRepeating(string):
    count = getCharCountArray(string)
    index = -1
    k = 0
 
    for i in string:
        if count[ord(i)] == 1:
            index = k
            break
        k += 1
 
    return index
 
# Driver program to test above function
string = "geeksforgeeks"
index = firstNonRepeating(string)
if index == 1:
    print ("Either all characters are repeating or string is empty")
else:
    print ("First non-repeating character is" , string[index])


# In[ ]:


#5. Write a program to implement Tower of Hanoi algorithm
def tower_of_hanoi(disks, source, auxiliary, target):  
    if(disks == 1):  
        print('Move disk 1 from rod {} to rod {}.'.format(source, target))  
        return  
    tower_of_hanoi(disks - 1, source, target, auxiliary)  
    print('Move disk {} from rod {} to rod {}.'.format(disks, source, target))  
    tower_of_hanoi(disks - 1, auxiliary, source, target)  
  
  
disks = int(input('Enter the number of disks: '))    
tower_of_hanoi(disks, 'A', 'B', 'C') 


# In[ ]:


#6.Write a program to convert postfix to prefix expression.
 #Read the Postfix expression from left to right
 #If the symbol is an operand, then push it onto the Stack
 #If the symbol is an operator, then pop two operands from the Stack 
 #Create a string by concatenating the two operands and the operator before them. 
 #string = operator + operand2 + operand1 
 #And push the resultant string back to Stack
 #Repeat the above steps until end of Postfix expression.
class Stack:
    def __init__(self,limit):
        self.limit = limit
        self.elements = []
        
    def push(self,number):
        if len(self.elements)== self.limit:
            print('stack is full')
        else:
            self.elements.append(number)
            
    def pop(self):
        if len(self.elements)==0:
            print('The stack is empty')
        else:
            #print(f'removing {self.elements[-1]} from the stack')
            return self.elements.pop()
            
    def peek(self):
        if len(self.elements)==0:
            print('The stack is empty')
        else:
            return self.elements[-1]
    
    def isEmpty(self):
        if len(self.elements)== 0:
            return True
        else:
            return False
        
    def isFull(self):
        if len(self.elements)==self.limit:
            return True
        else:
            return False
        def delete(self):
        self.elements=[]
        
        def print_stack(self):
        print('\n---------------- Current stack values ------------------\n')
        for item in self.elements:
            print(item,end=' ')
            
str1=input("enter the Postfix String")
stack1=Stack(len(str1))
list1=['*','%','+','/','^','-']
for i in str1:
    if i.isalpha():
        stack1.push(i)
    if i in list1:
        a=stack1.pop()
        b=stack1.pop()
        i=i+b+a
        stack1.push(i)
print(stack1.pop())
        


# In[ ]:


#7.program to convert prefix expression to infix expression.
  #Read the Prefix expression in reverse order (from right to left)
  #If the symbol is an operand, then push it onto the Stack
  #If the symbol is an operator, then pop two operands from the Stack 
  #Create a string by concatenating the two operands and the operator between them. 
  #string = (operand1 + operator + operand2) 
  #And push the resultant string back to Stack
  #Repeat the above steps until the end of Prefix expression.
  #At the end stack will have only 1 string i.e resultant string
class Stack:
    def __init__(self,limit):
        self.limit = limit
        self.elements = []
        
    def push(self,number):
        if len(self.elements)== self.limit:
            print('stack is full')
        else:
            self.elements.append(number)
            
    def pop(self):
        if len(self.elements)==0:
            print('The stack is empty')
        else:
            #print(f'removing {self.elements[-1]} from the stack')
            return self.elements.pop()
            
    def peek(self):
        if len(self.elements)==0:
            print('The stack is empty')
        else:
            return self.elements[-1]
    
    def isEmpty(self):
        if len(self.elements)== 0:
            return True
        else:
            return False
        
    def isFull(self):
        if len(self.elements)==self.limit:
            return True
        else:
            return False
         def delete(self):
        self.elements=[]
        
    def print_stack(self):
        print('\n---------------- Current stack values ------------------\n')
        for item in self.elements:
            print(item,end=' ')
            
str1=input("enter the Prefix String")
str1=str1[::-1]
stack1=Stack(len(str1))
list1=['*','%','+','/','^','-']
for i in str1:
    if i.isalpha():
        stack1.push(i)
    if i in list1:
        a=stack1.pop()
        b=stack1.pop()
        i=a+i+b
        stack1.push(i)
print(stack1.pop())


# In[ ]:


#8.program to check if all the brackets are closed in a given code snippet
#only check all brackest are closed or not ,not balanced or not
class Stack:
    def __init__(self,limit):
        self.limit = limit
        self.elements = []
        
    def push(self,number):
        if len(self.elements)== self.limit:
            print('stack is full')
        else:
            self.elements.append(number)
            
    def pop(self):
        if len(self.elements)==0:
            print('The stack is empty')
        else:
            #print(f'removing {self.elements[-1]} from the stack')
            return self.elements.pop()
            
    def peek(self):
        if len(self.elements)==0:
            print('The stack is empty')
        else:
            return self.elements[-1]
    
    def isEmpty(self):
        if len(self.elements)== 0:
            return True
        else:
            return False
        
    def isFull(self):
        if len(self.elements)==self.limit:
            return True
        else:
            return False
        
    def delete(self):
        self.elements=[]
        
    def print_stack(self):
         print('\n---------------- Current stack values ------------------\n')
        for item in self.elements:
            print(item,end=' ')

str1=input("enter the string")
list1=['(','{','[']
list2=[')','}',']']
stack1=Stack(len(str1))
flag=0
for i in str1:
    if i in list1:
        stack1.push(i)
    if i in list2:
        stack1.pop()
if stack1.isEmpty():
            print("All brackets are closed")
else:
    print("All brackets are NOT closed")   
    


# In[ ]:


#9. Write a program to reverse a stack.
class Stack:
    def __init__(self,limit):
        self.limit = limit
        self.elements = []
        
    def push(self,number):
        if len(self.elements)== self.limit:
            print('stack is full')
        else:
            self.elements.append(number)
            
    def pop(self):
        if len(self.elements)==0:
            print('The stack is empty')
        else:
            #print(f'removing {self.elements[-1]} from the stack')
            return self.elements.pop()
            
    def peek(self):
        if len(self.elements)==0:
            print('The stack is empty')
        else:
            return self.elements[-1]
    
    def isEmpty(self):
        if len(self.elements)== 0:
            return True
        else:
            return False
        
    def isFull(self):
        if len(self.elements)==self.limit:
            return True
        else:
            return False
         def delete(self):
        self.elements=[]
        
    def print_stack(self):
        print('\n---------------- Current stack values ------------------\n')
        for item in self.elements:
            print(item,end=' ')
        
def reverse_stack(str1):
    ch=[]
    for i in str1:
        stack1.push(i)
    while not stack1.isEmpty():
        stack2.push(stack1.pop())
        stack2.print_stack()
    while not stack2.isEmpty():
        ch.append(stack2.pop())
    return ch
            
str1=input("Enter the first string :")
str1=list(str1)
ch=[]
stack1=Stack(len(str1))
stack2=Stack(len(str1))
ch=reverse_stack(str1)
str2="".join(ch)
print("\nreverse of Stack:",str2)


# In[ ]:


#10. Write a program to find minimum element using a stack.
from collections import deque
 
class MinStack:
    def __init__(self):
        # main stack to store elements
        self.s = deque()
        # variable to store the minimum element
        self.min = None
 
    # Inserts a given element on top of the stack
    def push(self, val):
        if not self.s:
            self.s.append(val)
            self.min = val
        elif val > self.min:
            self.s.append(val)
        else:
            self.s.append(2*val - self.min)
            self.min = val
 
    # Removes the top element from the stack
    def pop(self):
        if not self.s:
            self.print('Stack underflow!!')
            exit(-1)
        top = self.s[-1]
        if top < self.min:
            self.min = 2*self.min - top
        self.s.pop()
 
    # Returns the minimum element from the stack in constant time
    def getMin(self):
        return self.min
 
 
if __name__ == '__main__':
 
    s = MinStack()
 
    s.push(6)
    print(s.getMin())
     s.push(7)
    print(s.getMin())
 
    s.push(5)
    print(s.getMin())
 
    s.push(3)
    print(s.getMin())
 
    s.pop()
    print(s.getMin())
 
    s.pop()
    print(s.getMin())
        

