#!/usr/bin/env python
# coding: utf-8

# In[1]:


num_friends=[100, 49, 41, 40, 25, 10, 5, 4, 7, 20, 60]


# In[2]:


def mean_num_friends(x):
    return sum(x) / len(x)


# In[9]:


print("mean={}".format(mean_num_friends(num_friends)))


#print("mean={}".format(mean_num_friends(num_friends))



# In[12]:


def median_num_friends(x):
    n = len(x)
    sorted_v = sorted(x)
    midpoint = n // 2
    if n % 2 == 1:
        return sorted_v[midpoint]
    else:
        lo = midpoint - 1
        hi = midpoint
        return (sorted_v[lo] + sorted_v[hi]) / 2


# In[13]:


print("median={}".format(median_num_friends(num_friends)))


# In[17]:


def normal_pdf(x, mu=0, sigma=1):
   sqrt_two_pi = math.sqrt(2 * math.pi)
   return (math.exp(-(x-mu) ** 2 / 2 / sigma ** 2) / (sqrt_two_pi * sigma))


# In[19]:


import math
from matplotlib import pyplot as plt
xs = [x / 10.0 for x in range(-50, 50)]
plt.plot(xs, [normal_pdf(x, sigma=1) for x in xs], '-', label='mu=0,sigma=1')
plt.plot(xs, [normal_pdf(x, sigma=2) for x in xs], '-', label='mu=0,sigma=2')
plt.plot(xs, [normal_pdf(x, sigma=0.5) for x in xs], '-', label='mu=0,sigma=0.5')
plt.plot(xs, [normal_pdf(x, sigma=-1) for x in xs], '-', label='mu=0,sigma=-1')
plt.legend()
plt.show()


# In[ ]:




