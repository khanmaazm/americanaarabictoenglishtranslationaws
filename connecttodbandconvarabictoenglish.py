#!/usr/bin/env python
# coding: utf-8

# In[71]:


import cx_Oracle
import requests


# In[39]:


import os
os.environ["NLS_LANG"] = "AMERICAN_AMERICA.AL32UTF8"
print(os.environ["NLS_LANG"])


# In[50]:


connection_string = "%s:%s/%s" % ("localhost", "1522", "xe")
print(connection_string)
con = cx_Oracle.connect("c##americanaprd", "americana", connection_string, encoding="UTF-8", nencoding="UTF-8")


# In[51]:


cursor = con.cursor()
print ("Connection Version: {}".format(con.version))
print(con.encoding)
print(con.nencoding)


# In[53]:


query = 'select name from vendors where vendor_id = 40145'
cursor.execute (query)
resultrecs = cursor.fetchone()
for r in resultrecs:
    print (r)
    print (type(r[0]))


# In[56]:


urlbase = 'https://k0rtmd4ue2.execute-api.us-east-1.amazonaws.com/default/americanatranslatetext?sourcelang=ar&targetlang=en&text='
texttoq='بالون ليدى'
finalurl = urlbase + texttoq
print(finalurl)
print(type(texttoq))
print(type(finalurl))


# In[57]:


for row in cursor.execute ('select name from vendors where vendor_id = 40145'):
    print(ord(row[0][0]),ord(row[0][1]),ord(row[0][2]),ord(row[0][3]))
    url = urlbase + row[0]
    print(row[0])
    print(url)
    response = requests.get(url)
    jsonoutput = response.json()
    print(jsonoutput["Translationoutput"]["TranslatedText"])
    url = urlbase + texttoq
    print(url)


# In[58]:


import pandas as pd


# In[65]:


xx=pd.read_csv('arabicvends.csv')


# In[62]:


urlbase = 'https://k0rtmd4ue2.execute-api.us-east-1.amazonaws.com/default/americanatranslatetext?sourcelang=ar&targetlang=en&text='


# In[72]:


for row in xx.iterrows():
    url=urlbase + row[1]["NAME"]
    print(url)
    response = requests.get(url)
    jsonoutput = response.json()
    print(jsonoutput["Translationoutput"]["TranslatedText"])    

