#!/usr/bin/env python
# coding: utf-8

# In[6]:


from nltk.corpus import webtext


# In[ ]:





# In[9]:


import nltk


# In[10]:


nltk.download('webtext')


# In[11]:


from nltk.corpus import webtext


# In[12]:


webtext.fileids()


# In[13]:


print(webtext.words(fileids='pirates.txt'))


# In[14]:


print(webtext.words(fileids='pirates.txt')):20


# In[17]:


for file in webtext.fileids():
    print(file, webtext.words(fileids=file)[:20])


# In[18]:


for file in webtext.fileids():
    print(file, webtext.words(fileids=file)[:20])


# In[20]:


import nltk 


# In[41]:


f = open('tweets1.txt', 'r')


# In[42]:


text = f.read()
print(text)


# In[43]:


text1 = text.split()


# In[44]:


text2 = nltk.Text(text1)


# In[38]:


print(text)


# In[46]:


text2.concordance("good")


# In[49]:


from urllib import request 


# In[53]:


url= "http://www.guttenberg.org/files/2554/2554-0.txt"


# In[74]:


response= request.urlopen(url)


# In[75]:


raw = response.read().decode('utf8')


# In[76]:


type(raw)


# In[78]:


len(raw)


# In[83]:


print(raw)


# In[ ]:




