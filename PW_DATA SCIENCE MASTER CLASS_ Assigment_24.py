#!/usr/bin/env python
# coding: utf-8

# # Assignment_ 25-02-2023

# ## 1. Write a code to print the data present in the second row of the dataframe,df.
# 
# ### Ans:-

# In[1]:


import pandas as pd


# In[2]:


course_name = ['Data Science','Machine Learning','Big Data','Data Engineer']
duration = [2,3,6,4]


# In[3]:


df = pd.DataFrame(data ={'course_name':course_name,'duration':duration})


# In[4]:


df


# In[5]:


print(df.iloc[1])


# In[6]:


print(df.loc[1])


# ## 2. Write is the difference between the functions loc and iloc in pandas Data frame?
# 
# ### Ans:-
# 
#         Both loc and iloc are used to index and select data from a Pandas DataFrame, but they work differently:
# 
# ## loc: 
#         This function is used to select rows based on the row label or index, and columns based on the column label. For 
#         example, df.loc[2:4, 'column_name'] selects rows 2 through 4 and the column named 'column_name'. The index must be a
#         label-based index (either a string or an integer index that corresponds to a label).
# 
# ## iloc: 
#         This function is used to select rows and columns based on their integer position in the DataFrame. For example, 
#         df.iloc[2:4, 0:2] selects rows 2 through 4 and columns 0 through 2 (excluding the last column, which has index 2).
#         The index must be a positional index (an integer that corresponds to the position of the row or column in the 
#         DataFrame).
#         
# ## The differences between loc and iloc:-
# 
#                   loc                                                                iloc
#     ------------------------------------------------------------------------------------------------------------------------
#     1. loc select rows and columns based on their label                1. iloc selects them based on their integer position.
#     2. loc is inclusive of the end point of the range specified.       2. iloc is exclusive of the end point of the range 
#                                                                           specified.
#     3. loc can only be used with label-based indexes.                  3. iloc can only be used with positional indexes.
#     4. loc is slower than iloc especially when dealing with large      4. iloc is fater then loc.
#        Data Frame, because it involves label-based indexing and 
#        required more memory to store the labels.

# ## 3. Reindex the given data frame using the variable , reindex=[3,0,1,2] and store it in the variable ,new_df then find the output for both new_df.loc[2] and new_df.iloc[2]. Did you observe any difference in both the outputs ? if so then explain it.
# 
# ### Ans:-

# In[7]:


import pandas as pd
import numpy as np


# In[8]:


columns = ['column_1','column_2','column_3','column_4','column_5','column_7']
indices = [1,2,3,4,5,6]


# In[9]:


df1 = pd.DataFrame(np.random.rand(6,6),columns= columns,index = indices)


# In[10]:


df1


# In[11]:


new_df = df1.reindex([3,0,1,2])
print(new_df)


# In[12]:


new_df.loc[2]


# In[13]:


new_df.iloc[2]


# ####  In general, the difference between loc and iloc is that loc is used to select rows and columns by label, while iloc is used to select rows and columns by integer position.

# ## 4. write a code to find the following statictical measurments for the above dataframe df1.  (i) mean of each and every column present in the data frame.                                                      (ii) standard devation of column,'column_2'.
# 
# ### Ans:-

# In[14]:


columns = ['column_1','column_2','column_3','column_4','column_5','column_7']
indices = [1,2,3,4,5,6]
df1 = pd.DataFrame(np.random.rand(6,6),columns= columns,index = indices)
print(df1)


# In[15]:


## Mean of each and every column present in the data frame
print(df1.mean()) 


# In[16]:


## standard devation of column,'column_2'.
print(df1['column_2'].std())


# ## 5. Replace the data present in the second row of column_2 by a string variable then find the mean of the column,column_2. if you getting errors in executing it then explain why. [Hint: To replace the data use df1.loc[ ] and equate this to string data of your choice]
# 
# ### Ans:-

# In[17]:


columns = ['column_1','column_2','column_3','column_4','column_5','column_7']
indices = [1,2,3,4,5,6]
df1 = pd.DataFrame(np.random.rand(6,6),columns= columns,index = indices)
df1.loc[2,'column_2']= 'Manas Pandey'


# In[18]:


mean_column_2 = df1['column_2'].mean()
print(mean_column_2)


# ## 
#        This is because mean() cannot be computed on a column that has mixed data types. If you want to compute the mean of 
#        column_2, you need to convert the string value to a numeric value first. If the column has many rows, you may need to
#        manually convert each value to a numeric type using pd.to_numeric().

# ## 6. What do you understand about the windows function in pandas and list the types of windows function?
# 
# ### Ans:-
#      In pandas, a window function is a way to perform calculations on a subset of rows from a DataFrame or a Series, based 
#      on a sliding or expanding window. The window is defined by a set of rows, called the "window size" or "window length,"
#      that move across the DataFrame or Series.
#      
#      Window functions are useful for performing calculations that require looking at a subset of rows instead of individual
#      rows, such as calculating moving averages, cumulative sums, or rank-based statistics. They can be applied using the
#      .rolling() or .expanding() methods in pandas.
#      
#      The types of window functions that can be used with pandas are:
#      
#      1.Rolling Window Functions:- These functions compute statistics over a sliding window of a fixed size. They are applied
#      using the .rolling() method, which creates a rolling window object, on which you can apply aggregation methods 
#      like sum(), mean(), std(), min(), max(), etc.
#      
#      2.Expanding Window Functions:- These functions compute statistics over an expanding window, which starts at the 
#      beginning of the data and includes all preceding rows up to the current row. They are applied using the .expanding()
#      method, which creates an expanding window object, on which you can apply aggregation methods like sum(), mean(), std(),
#      min(), max(), etc.
#      
#      3.Exponentially Weighted Window Functions:- These functions compute statistics over a weighted window, in which more 
#      recent values are given more weight than older values. They are applied using the .ewm() method, which creates an 
#      exponentially weighted window object, on which you can apply aggregation methods like mean(), std(), etc.
#      
#      4.GroupBy with Window Functions:- These functions group data by one or more columns and then apply a window function to
#      each group separately. They are applied using the .groupby() method with the .rolling(), .expanding(), or.ewm()methods.

# ## 7. Write a code to print only the current month and year at the time of answering this Question. [Hint :- using pandas Datetime function]
# 
# ### Ans:-

# In[19]:


import datetime


# In[20]:


now = datetime.datetime.now()


# In[21]:


current_month = now.strftime("%B")
current_year  = now.year
print("current month and year:  ",current_month,current_year)

""""This code first imports the datetime module and creates a datetime object called current_time that represents 
    the current date and time. It then uses the strftime() method to format the datetime object as a string 
    that only includes the month name and the year. Finally, it prints the resulting string to the console."""


# ## 7. Write a Python Program that takes in two dates as inputs (in the format YYYY-MM-DD) and calculate the different between them in days,hours, and minutes using pandas time delta. The program should prompt the user to enter the dates and display the result.
# 
# ### Ans:-

# In[22]:


import pandas as pd


# In[24]:


date1 = input("Enter the first date in YYYY-MM-DD format:  ")
date2 = input("Enter the second date in YYYY-MM-DD format: ")

date1 = pd.to_datetime(date1)
date2 = pd.to_datetime(date2)

diff = date2-date1

## Extract days, hours, and minutes from timedelta object
days = diff.days
hours = diff.seconds // 3600

minutes = (diff.seconds%3600)//60

print (f"The different between {date1.date()} and {date2.date()} is {days} days,{hours} hours,{minutes} minutes")



# ## 9. Write a Python Program that read csv file containing categorical data and convert a specified column to a categorical data type. The program should be prompt the user to enter the file path, column name and category order and display the sorted data.
# 
# ### Ans:-

# In[2]:


import pandas as pd


# In[3]:


print(pd.__version__)


# In[1]:


import pandas as pd


# In[5]:


df=pd.read_csv('object_data.csv')


# In[6]:


df.head()


# In[24]:


file_path = input("Enter the file path: ")
column_name = input("Enter the column name: ")
Category_order= input( "Enter the category order:  ").split(',')

df = pd.read_csv(file_path)

df[column_name]=pd.Categorical(df[column_name],categories=Category_order)
df_sorted = df.sort_values(column_name)

print(df_sorted)


# In[27]:


file_path = input("Enter the file path: ")
column_name = input("Enter the column name: ")
Category_order= input( "Enter the category order:  ").split(',')

df = pd.read_csv(file_path)

df[column_name]=pd.Categorical(df[column_name],categories=Category_order)
df_sorted = df.sort_values(column_name)

print(df_sorted)


# In[28]:


file_path = input("Enter the file path: ")
column_name = input("Enter the column name: ")
Category_order= input( "Enter the category order:  ").split(',')

df = pd.read_csv(file_path)

df[column_name]=pd.Categorical(df[column_name],categories=Category_order)
df_sorted = df.sort_values(column_name)

print(df_sorted)


# ## 10.Write a Python that reads a csv file containing sales data for different products and visualizes the data using a stacked bar chart to show the sales of each product category over time. The program prompt the user to enter the file path and display the chart.
# 
# ### Ans:-
# 

# In[31]:


import pandas as pd
import matplotlib.pyplot as plt


# In[32]:


sales_df=pd.read_csv('SalesData.csv')


# In[33]:


sales_df.head()


# In[34]:


sales_df


# In[41]:


sales_df.columns


# In[42]:


print(sales_df.columns)


# In[43]:


sales_df['Date ']=pd.to_datetime(sales_df['Date '])


# In[58]:


file_path = input('Enter the file path for the CSV file:  ')
sales_df = pd.read_csv(file_path)
sales_df['Date '] = pd.to_datetime(sales_df['Date '])
x=sales_df['Date ']
y=sales_df['Sales Count']
plt.figure(figsize=(10,6))
plt.bar(x,y,color = '#7E10D5')
plt.xlabel("Date")
plt.ylabel("SalesCount")
plt.title("sales by product Category")
plt.grid()
plt.show()


# ## 11.You are given a CSV file containing student data that includes the student ID and their test Score. Write a python program that reads the CSV file,calculates the mean,median,and mode of the test scores and displays the results in a table.
# 
# ### Ans:-

# In[59]:


studentdata_df=pd.read_csv('studentdata.csv')


# In[60]:


studentdata_df


# In[79]:


file_path = input("Enter the Student Data CSV file: ")
studentdata_df=pd.read_csv(file_path)
mean_score = studentdata_df['Test Score'].mean()
median_score =studentdata_df['Test Score'].median()
mode_score = studentdata_df['Test Score'].mode()[0]
results = pd.DataFrame({'Statistic':['Mean','Midean','Mode'],'value':[mean_score,median_score,mode_score]})
print(results)


# In[1]:


import pandas as pd
file_path = input("Enter the Student Data CSV file: ")
studentdata_df = pd.read_csv(file_path)
mean_score = studentdata_df['Test Score'].mean()
median_score = studentdata_df['Test Score'].median()
mode_score = studentdata_df['Test Score'].iloc[0]
results = pd.DataFrame({'Statistic':['Mean','Midean','Mode'],'value':[mean_score,median_score,mode_score]})
print(results)


# In[ ]:




