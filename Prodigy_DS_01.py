#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


df=pd.read_csv("C:/Users/Rajesh Gonnade/Desktop/world bank.csv")
print(df.head())


# In[3]:


# size of the DataFrame
df.shape


# In[4]:


df.dtypes


# In[5]:


df.describe()


# In[6]:


df.info()


# In[7]:


df.isnull().sum()


# In[8]:


#dropping rows (axis=0) from the DataFrame df where at least one element is missing (NaN)
df.dropna(axis=0, how='any', inplace=True)
df


# In[9]:


df.info()


# In[10]:


data = df.drop(['Country Code','Indicator Name','Indicator Code'],axis=1)
data


# In[11]:


data.columns


# In[12]:


#years from 1960 to 2022
cols = [str(year) for year in range(1960, 2023)]

for col in cols:
        # Create a figure for each year
        fig = plt.figure(figsize =(5, 5))
        #Histogram
        plt.hist(data[col],color='green',bins=10)
        plt.xlabel(col)
        plt.title(f"Histogram for {col}")
        # Show Plot
        plt.show()
 


# In[13]:


#plotting bar plot from 1960 to 2022
years = [str(year) for year in range(1960, 2023)]
Total_count=data[years].sum()

plt.figure(figsize=(15,15))
# Bar plot
plt.barh(years,Total_count,color='purple')
plt.xlabel("Total")
plt.ylabel("Year",size=20)
plt.title("Total count per year",size=15)
plt.show()


# In[14]:


# Sort the DataFrame by the '1960' column in descending order and select the top 10 countries

    
top_10_countries=data.sort_values(by='1960',ascending=False).head(10)
top_10_countries

top_10_countries_t=top_10_countries.set_index('Country Name').T
for country_name,data_values in top_10_countries_t.iterrows():
    fig=plt.figure(figsize=(5,5))
    sns.barplot(x=data_values.index,y=data_values.values)
    plt.xlabel("Countries")
    plt.ylabel("Values")
    plt.title(f"{country_name}- Values from 1960 to 2022")
    plt.xticks(rotation=60)
    # Show Plot
    plt.show()


# In[ ]:




