#!/usr/bin/env python
# coding: utf-8

# In[40]:


import pandas  as pd
df=pd.read_csv('Students_Performance.csv')


# In[41]:


# 1 a)Find out how many males and females participated in the test.
df['gender'].value_counts()


# In[42]:


# 1 b) What do you think about the students' parental level of education?
df['parental level of education'].value_counts()


# Most of the parents have education from some college.Very few have masters degree.

# In[48]:


# 1 c)Who scores the most on average for math, reading and writing based on gender

y=df.groupby('gender')[['math score','reading score','writing score']].mean()
y


# In[49]:


# c.i.) Based on Gender
y.idxmax()


# In[50]:


# c.ii)
x=df.groupby('test preparation course')[['math score','reading score','writing score']].mean()
x


# In[51]:


# c.ii) based on test preparation course
x.idxmax()


# Base on gender,male got the highest math score and frmale got highest in reading and writing score
# Base on test preparation course,those who completed the course got highest in all 3 sections

# In[58]:


# d.)What do you think about the scoring variation for math, reading and writing based on
# d.i)Based on Gender
df.groupby('gender')[['math score','reading score','writing score']].agg(['max','min','mean','std'])


# In[59]:


# d.ii) Based on test preparation course
df.groupby('test preparation course')[['math score','reading score','writing score']].agg(['max','min','mean','std'])


# In[63]:


# e) The management needs your help to give bonus points to the top 25% of students based on their math score, so how will you help the management to achieve this.
top=0.25*len(df)
df_mathrank=df.sort_values(by='math score',ascending=False)
df_mathrank.head(int(top))


# Case Study on Testing of Hypothesis

# In[64]:


df_sales=pd.read_csv('Sales_add.csv')
df_sales.columns


# In[9]:


#2 a)The company wishes to clarify whether there is any increase in sales after stepping into digital marketing.
pop_mean=df_sales['Sales_before_digital_add(in $)'].mean()
sample_size=len(df_sales['Sales_After_digital_add(in $)'])
sample_mean=df_sales['Sales_After_digital_add(in $)'].mean()
sample_std=df_sales['Sales_After_digital_add(in $)'].std()
alpha=0.05
data=df_sales['Sales_After_digital_add(in $)']
print(f'pop_mean={pop_mean},sample_size={sample_size},sample_mean={sample_mean},sample_std={sample_std},alpha=0.05')


# As sample size <30,t-test can be used
# H0 = There is no increase in sales after stepping in to digital marketing
# H1=Sales increased after digital marketing
# 

# In[65]:


import scipy.stats as stats
t_stat,p_value=stats.ttest_1samp(data,pop_mean,alternative='greater')
print(t_stat,p_value)


# In[66]:


if p_value<alpha:
    print('Reject null hypothesis.There is an increase in sales after stepping in to digital marketing')
else:
    print('Fail to reject null hypothesis.There is no increase in sales after stepping in to digital marketing')


# In[70]:


# 2 b)The company needs to check whether there is any dependency between the features “Region” and “Manager”.

from scipy.stats import chi2_contingency
table=pd.crosstab(df_sales['Region'],df_sales['Manager'])
chi2_stat,p_value,dof,expected=stats.chi2_contingency(table)
print(chi2_stat,p_value,dof,expected)


# In[71]:


if p_value<alpha:
    print('Reject null hypothesis.There is dependency between the objects')
else:
    print('Fail to reject null hypothesis.There is no dependency between 2 objects')


# In[ ]:




