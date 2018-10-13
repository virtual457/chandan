
# coding: utf-8

# In[50]:


from scipy import ndimage
import matplotlib.pyplot as plt


# In[51]:


get_ipython().magic('matplotlib inline')


# In[52]:


import numpy as np


# In[53]:


from sklearn.preprocessing import normalize


# In[164]:


img = plt.imread('/home/manur/Downloads/333.jpg')


# In[165]:


x,y,_ = img.shape


# In[166]:


i1 = normalize(np.resize(img[:,:,0],(x,y)),norm='max')


# In[169]:


i2 = ndimage.convolve(i1,[[0,-1,0],[-1,2,-1],[0,-1,0]],mode='constant',cval=0.0)


# In[171]:


t = (i2.min()+i2.max())/2


# In[172]:


i3 = []

for i in i2:
    temp = []
    for j in i:
        if(j<=t):
            temp.append(0.)
        else:
            temp.append(1.)
    i3.append(temp)


# In[174]:


plt.imshow(i3,cmap='gray')
plt.show()

# In[ ]:





# In[ ]:




