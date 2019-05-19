#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2


# In[2]:


x=cv2.VideoCapture(0)


# In[3]:


ret,photo=x.read()


# In[4]:


cv2.imshow("First",photo)
cv2.waitKey()
cv2.destroyAllWindows()


# In[5]:


x.release()


# In[6]:


x=cv2.VideoCapture(0)


# In[7]:


ret_3,photo_3=x.read()


# In[8]:


cv2.imshow("Second",photo_3)
cv2.waitKey()
cv2.destroyAllWindows()


# In[9]:


photo.shape


# In[10]:


photo_3.shape


# In[11]:


n=photo_3[50:200,100:400]


# In[12]:


cv2.imshow("New",n)
cv2.waitKey()
cv2.destroyAllWindows()


# In[13]:


x.release()


# In[14]:


photo[100:250,200:500]=n


# In[15]:


cv2.imshow("Updated Photo",photo)
cv2.waitKey()
cv2.destroyAllWindows()


# In[ ]:




