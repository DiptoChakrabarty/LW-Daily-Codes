#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2


# In[16]:


cap=cv2.VideoCapture(0)


# In[17]:


while True:
    ret,photo=cap.read()
    ret2,p=cv2.threshold(photo,151,255,cv2.THRESH_BINARY)
    cv2.imshow("Video",p)
    if cv2.waitKey(1) == 13:
        break
cv2.destroyAllWindows()


# In[18]:


cap.release()


# In[ ]:




