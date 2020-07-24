#!/usr/bin/env python
# coding: utf-8

# In[1]:


list2=[10,20,40,60,70,80]



list2.sort(reverse=1)


# In[3]:


print(list2)


# In[4]:


list3 = [(10,4),(2,4),(6,7),(2,6)]


# In[5]:


def fun1(x):
    return x[0]+x[1]
list3.sort(key=fun1)
print (list3)


# In[ ]:




