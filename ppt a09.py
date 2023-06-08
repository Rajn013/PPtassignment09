#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Answer 1

def isPowerTwo(n):
    if n <= 0:
        return False
    return(n & (n - 1)) == 0


# In[2]:


print(isPowerTwo(1))


# In[3]:


print(isPowerTwo(18))


# In[4]:


print(isPowerTwo(6))


# In[5]:


print(isPowerTwo(16))


# In[6]:


print(isPowerTwo(3))


# In[7]:


#answer 2

def NaturalNumber(n):
    return n * (n + 1) // 2


# In[8]:


print(NaturalNumber(3))


# In[9]:


print(NaturalNumber(5))


# In[12]:


#answer 3

def factorial(N):
    if N == 0:
        return 1
    else:return N * factorial(N - 1)


# In[13]:


print(factorial(5))


# In[14]:


print(factorial(4))


# In[15]:


#answer 4

def power(n , p):
    return n ** p


# In[16]:


print(power(5, 2))


# In[17]:


print(power(2, 5))


# In[18]:


#answer 5

def findMax(arr):
    if len(arr) == 1:
        return arr[0]
    else:
        return max(arr[0], findMax(arr[1:]))


# In[19]:


arr1 = [1, 4, 3, -5, -4, 8, 6]
arr2 = [1, 4, 45, 6, 10, -8]

print(findMax(arr1))
print(findMax(arr2))


# In[21]:


#answer 6 

def NthTerm(a, d, N):
    return a + (N - 1) * d


# In[23]:


a1 = 2
d1 = 1
N1 = 5
print(NthTerm(a1, d1, N1))


# In[25]:


a2 = 5
d2 = 2
N2 = 10
print(NthTerm(a2, d2, N2))


# In[6]:


#Answer 7


from itertools import permutations

def permute(s):
    return [''.join(p) for p in permutations(s)]


# In[7]:


S = "ABC"
print(permute(S))

S = "XY"
print(permute(S))


# In[8]:


#Answer 8

def product_of_array(arr):
    product = 1
    for num in arr:
        product *= num
    return product


# In[9]:


arr = [1, 2, 3, 4, 5]
print(product_of_array(arr))


# In[11]:


arr = [1, 6, 3]
print(product_of_array(arr))


# In[ ]:




