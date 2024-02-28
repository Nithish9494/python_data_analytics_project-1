#!/usr/bin/env python
# coding: utf-8

# In[1]:


#https://www.kaggle.com/datasets/aiaiaidavid/the-big-dataset-of-ultra-marathon-running?resource=download


# In[2]:


#import libraries


# In[5]:


import pandas as pd


# In[6]:


import seaborn as sns


# In[75]:


df = pd.read_csv("TWO_CENTURIES_OF_UM_RACES.csv")


# In[ ]:


#see the data that's been imported


# In[91]:


df.head(10)


# In[78]:


df.shape


# In[89]:


df.dtypes


# In[80]:


#clean up data


# In[81]:


#Only want USA Races, 50k or 50mi,2020


# In[82]:


# step 1 show 50mi or 50k
#50km
#50mi


# In[92]:


df[df['Event distance/length'] == '50km']


# In[84]:


#combine 50km &50mi in the year 2020


# In[85]:


df[(df['Event distance/length']. isin (['50km','50mi']))  & (df['Year of event']== 2020)]


# In[86]:


# 50km or 50mi in usa


# In[95]:


df[df['Event name'].str.split('(').str.get(1).str.split(')').str.get(0) =='USA']


# In[96]:


# combine all the filters together


# In[97]:


df[(df['Event distance/length']. isin (['50km','50mi']))  & (df['Year of event']== 2020) & (df['Event name'].str.split('(').str.get(1).str.split(')').str.get(0) =='USA')]


# In[118]:


df2 = df[(df['Event distance/length']. isin (['50km','50mi']))  & (df['Year of event']== 2020) & (df['Event name'].str.split('(').str.get(1).str.split(')').str.get(0) =='USA')]


# In[119]:


df2.head(10)


# In[120]:


df2.shape


# In[103]:


#Remove (USA) from event name


# 

# In[ ]:


#Remove h from athlete perfomance


# In[153]:


df2['Athlete performance'] = df2['Athlete performance'].str.strip(' ').str.get(0)


# In[154]:


df2.head(10)


# In[155]:


#drop coloumns: Athlete club, Athlete country,Athlete year of birth,Athlete age category


# In[158]:


df2 = df2.drop(['Athlete club','Athlete country','Athlete year of birth'] ,axis = 1)


# In[159]:


df2.head()


# In[131]:


#clean up null


# In[133]:


df2.isna().sum()


# In[138]:


df2 = df2.dropna()


# In[139]:


df2.shape


# In[140]:


#check for dupes


# In[144]:


df2 = df2.drop_duplicates()


# In[145]:


df2.shape


# In[146]:


#reset index


# In[147]:


df2.reset_index(drop = True)


# In[148]:


# fix types


# In[160]:


df2.dtypes


# In[161]:


df2['Athlete average speed'] = df2['Athlete average speed'].astype(float)


# In[162]:


#rename coloumns


# In[172]:


df2 = df2.rename(columns = {'Year of event':'year',
                        'Event dates':'race_day',
                        'Event distance/length':'race_length',
                        'Event number of finishers':'race_number_of_finishers',
                        'Athlete perfomance':'athelete_perfomance',
                        'Athlete average speed':'athlete_average_speed',
                        'Athelete ID':'athlete_id'
                        })


# In[174]:


df.head()


# In[188]:


df['Event distance/length']


# 

# In[197]:





# In[186]:


#plot a graph


# In[198]:


sns.histplot(df2['race_length'])


# In[ ]:





# In[ ]:





# In[ ]:




