#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# #1.	Load both the datasets.

# In[2]:


country = pd.read_csv("C:\Python Project\BIProject1\countryData.csv")


# In[3]:


immun = pd.read_csv("C:\Python Project\BIProject1\immunitizationData.csv")


# #2.	Explore the shapes and the dataset with .head()

# In[5]:


country.head()


# In[6]:


immun.head()


# Check missing values in all datasets.

# In[8]:


country.isnull()


# In[9]:


country.isnull().sum()


# In[10]:


immun.isnull()


# In[11]:


immun.isnull().sum()


# Check duplicate values in all datasets.

# In[13]:


country.duplicated()


# In[14]:


country.duplicated().sum()


# In[15]:


immun.duplicated()


# In[16]:


immun.duplicated().sum()


# Analyze descriptive statistics.

# In[18]:


country['Total expenditure'].max()


# In[19]:


country['Total expenditure'].min()


# ## Task 2

# ### Merge both data sets

# In[22]:


country.head(2)


# In[23]:


immun.head(2)


# In[24]:


a = pd.merge(country,immun, on="Country",how="inner")


# In[25]:


a.drop_duplicates()


# In[26]:


a.dtypes


# In[27]:


# categorical & continuous data types
catg = a.select_dtypes("object")
cont = a.select_dtypes("number")


# In[28]:


print(catg)


# In[29]:


print(cont)


# In[30]:


#3.	Impute missing value.
a.isnull().sum()


# # Scenario2

# ### Univariate analysis
# 

# In[33]:


a.shape


# In[34]:


a.info()


# In[35]:


a.describe()


# In[36]:


a.columns


# In[37]:


a


# In[38]:


sns.barplot(data=a,x='Year_x',y='Polio')


# In[39]:


sns.barplot(data=a,x='Year_y',y='Polio')


# In[40]:


sns.lineplot(data=a,x='Year_y',y='infant deaths')


# In[41]:


sns.lineplot(data=a,x='Year_x',y='Population')


# In[42]:


sns.lineplot(data=a,x='Year_x',y='Adult Mortality')


# In[43]:


sns.histplot("Life expectancy")


# ## bivariate analysis

# In[45]:


#a.	Find the highly correlated variables.
Corr_matrix=a.corr().round(2)
Corr_matrix


# In[46]:


sns.heatmap(a.corr().head(10), cmap = 'coolwarm')
plt.figure(figsize=(10,100))


# In[47]:


#i.	Does GDP per capita of the country impact life expectancy?
Corr_matrix["GDP"]

#Ans:- Yes GDP of the country impact life expectancy as it shows positive correation of 0.46 with each other


# In[48]:


#ii.	Does the Productive use of resources(Income composition of resources) make life expectancy better?
Corr_matrix["Income composition of resources"].head(5)
#ans:- as life expectancy and Income composition resources are highly & positively corelated with each other. so productive use 
#of resoursec make life expectancy better. 


# In[49]:


# iii.	Does Schooling impact life expectancy any better?
Corr_matrix["Schooling"].head(5)
# Ans :- Yes Schooling makes better life expectancy as both variables are highly correlated with each other.


# # Multivariate Analysis

# a.	Which diseases are correlated with life expectancy?

# In[52]:


Corr_matrix
# ans:- As per the below matrix 
#(1) Polio is positively correlated with life expectancy 
#(2) Diphtheria is positively correlated with life expectancy
#(3) HIV/AIDS is negatively correlated with life expecatancy 


# b.	Does better immunization coverage improve life expectancy?

# c.	How do countries' economic conditions affect life expectancy?

# In[58]:


Corr_matrix["GDP"].head(2)
# Ans:- GDP is positively corelated with Life expectancy So yes its affects. 


# # Task 2:

# a.	Calculate the average life expectancy of all the years and find out Top and Bottom countries.

# In[75]:


a.sort_index()


# b.Rank countries based on their average life expectancy.
# 

# In[85]:


Rank = a.groupby('Year_x')
Rank.first()


# c.Compare a few country’s life expectancies.
# 

# In[83]:


Comp_country = a.iloc[:, [0,1,3]]
Comp_country


# d.Compare life expectancy of Developed vs Developing country.
# 

# In[84]:


Compare = a.groupby('Status')
Compare.first()


# In[110]:


a.rename(columns={'Country':'Nations_1'}, inplace=True)
a


# Should a country having a lower life expectancy value(<65) increase its healthcare expenditure to improve its average lifespan?
# 

# Does Life Expectancy have a positive or negative correlation with eating habits(BMI), lifestyle, exercise, smoking, drinking alcohol, etc?
# 

# In[131]:


Corr_matrix
# YES Life Expectancy have a positive or negative correlation with eating habits(BMI), lifestyle, exercise, smoking, drinking alcohol, etc


# Do densely populated countries tend to have a lower life expectancy? (Hint : Take 2 densely populated countries like India, and Usa)
# 

# In[137]:


Comp_country = a.iloc[:, [0,1,3]]
Comp_country


# # END
